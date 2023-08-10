import shotgun_api3 as SG


def apikey():
    sgkey = SG.Shotgun('https://testvfx.shotgrid.autodesk.com ', 'testscript', 'byjzbl-abBmd3ohtpebhjkadu')
    return sgkey