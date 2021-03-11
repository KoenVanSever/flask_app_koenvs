from app import app

#! --------
#! NOT USED
#! --------


def calculate_df(df, material, init_perm, drive_level):
    """
    Calculates the procentual value remaining permeability at certain drive level H (in Oersted)
    Formula %µi = 1/(a + b * H ^ c)

    Args:
        material (string):
            Description of core material ('MPP', 'XFlux', 'Kool Mµ', 'High Flux', 'Kool Mµ MAX',
        'Kool Mµ E-core, U-core, Block', 'XFlux EQ & LP',
        'XFlux E-core, U-core, Block', 'High Flux EQ & LP', 'Kool Mµ EQ & LP',
        '75-Series', 'High Flux Special', 'Edge', 'Kool Mµ Hƒ')
        init_perm (int): Initial permeability (depending on core material)
        drive_level (int/float/iterable): drive level can be single value or iterable

    Returns:
        float/list: return object depending on drive_level type (float or iterable)

    Exception:
        AttributeError: calculated value is out of range
    """
    config = df[df.material == material][df.perm == init_perm]
    a = float(config.a)
    b = float(config.b)
    c = float(config.c)
    if hasattr(drive_level, "__iter__"):
        last = 1 / (a + b * pow(drive_level[len(drive_level) - 1], c)
        if last < 0.3:
            raise AttributeError("calculated value is out of range")
        # print("iterable")
        return [1 / (a + b * pow(x, c)) for x in drive_level]
    else:
        # print("not interable")
        calc=1 / (a + b * pow(drive_level, c))
        if calc < 0.3:
            raise AttributeError("calculated value is out of range")
        return 1 / (a + b * pow(drive_level, c))
