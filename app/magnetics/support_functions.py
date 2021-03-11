
def get_specific_factors(mat, perm, target_values, target_dict, search_dict, name):
    subset = search_dict[(search_dict.material == mat) & (search_dict.perm == int(perm))][target_values]
    target_dict[name] = subset.reset_index().drop("index", axis=1).loc[0].to_dict()
    return target_dict
