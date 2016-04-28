# This is an example template for Library Assemblies

import fd

# Store Assembly references at top of file as constants
DEFAULT_MATERIAL = ("Plastics","White Melamine")

class Material_Pointers():
    
    My_Material_Pointer = fd.Material_Pointer(DEFAULT_MATERIAL)

class Cutpart_Pointers():
    
    My_Cutpart_Pointer = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                            core="My_Material_Pointer",
                                            top="My_Material_Pointer",
                                            bottom="My_Material_Pointer")
    
class Edgepart_Pointers():
    
    My_Edgepart_Pointer = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                              material="My_Material_Pointer")