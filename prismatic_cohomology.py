import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.linalg import svd

def compute_composite_macro_factor(macro_df):
    """Compute composite macro factor from all macro variables."""
    if len(macro_df) < 2:
        return np.ones(len(macro_df)) * 0.5
    scaler = StandardScaler()
    macro_scaled = scaler.fit_transform(macro_df)
    pca = PCA(n_components=1)
    factor = pca.fit_transform(macro_scaled).flatten()
    factor = (factor - factor.min()) / (factor.max() - factor.min() + 1e-8)
    return factor

def p_adic_valuation_scaled(x, p=2):
    """Compute p-adic valuation scaled to [0,1]."""
    if x == 0:
        return 0
    x = int(round(abs(x) * 1000))
    if x == 0:
        return 0
    v = 0
    while x % p == 0:
        v += 1
        x //= p
    return min(v, 10) / 10.0

def prismatic_embedding(returns, p=2, dim=15):
    """
    Embed returns into the prismatic cohomology space.
    This unifies étale, crystalline, and de Rham cohomologies.
    """
    if len(returns) < 5:
        return np.zeros(dim)
    # Compute different cohomological invariants
    invariants = []
    # 1. de Rham cohomology: moments of the distribution
    for k in range(1, 6):
        invariants.append(np.mean(returns ** k))
    # 2. Crystalline cohomology: p-adic valuations
    valuations = np.array([p_adic_valuation_scaled(r, p) for r in returns])
    invariants.extend([
        np.mean(valuations),
        np.std(valuations),
        np.percentile(valuations, 50),
        np.percentile(valuations, 90)
    ])
    # 3. Étale cohomology: topological features (persistent homology proxy)
    # Use the variation of returns as a proxy for étale structure
    diff = np.diff(returns)
    invariants.extend([
        np.mean(np.abs(diff)),
        np.std(diff),
        np.percentile(diff, 75),
        np.percentile(diff, 95)
    ])
    # 4. Prismatic unification: combine all invariants
    prismatic = np.array(invariants[:dim])
    if len(prismatic) < dim:
        prismatic = np.pad(prismatic, (0, dim - len(prismatic)), 'constant')
    # Normalise
    if np.linalg.norm(prismatic) > 0:
        prismatic = prismatic / np.linalg.norm(prismatic)
    return prismatic

def prismatic_cohomology_rank(returns, macro_factor, p=2, dim=15, unification_levels=5):
    """
    Compute the prismatic cohomology rank: a unified measure of cohomological structure.
    """
    if len(returns) < 10:
        return 0
    # Compute prismatic embedding for each half of the data
    half = len(returns) // 2
    prism1 = prismatic_embedding(returns[:half], p, dim)
    prism2 = prismatic_embedding(returns[half:], p, dim)
    # Compute the prismatic pairing (unification of cohomologies)
    # This is the inner product in the prismatic space
    pairing = np.dot(prism1, prism2)
    # Scale by macro factor
    pairing = pairing * (1 + macro_factor * 0.5)
    # Rank = absolute value of pairing (higher = more unified structure)
    rank = abs(pairing)
    return rank

def prismatic_score(returns, macro_df, p=2, dim=15, unification_levels=5):
    """
    Compute per-ETF prismatic cohomology score.
    Higher score = more universal cohomological structure.
    """
    if len(returns) < 15 or macro_df is None or len(macro_df) < 15:
        return 0.0
    # Align lengths
    min_len = min(len(returns), len(macro_df))
    returns = returns[:min_len]
    macro_df = macro_df.iloc[:min_len]
    # Remove NaN
    mask = ~(np.isnan(returns) | np.isnan(macro_df).any(axis=1))
    returns = returns[mask]
    macro_df = macro_df[mask]
    if len(returns) < 15:
        return 0.0
    # Compute macro factor
    macro_factor = compute_composite_macro_factor(macro_df)[-1]
    # Compute prismatic cohomology rank
    rank = prismatic_cohomology_rank(returns, macro_factor, p, dim, unification_levels)
    return float(rank)
