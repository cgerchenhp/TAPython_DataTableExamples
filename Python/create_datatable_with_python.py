import unreal

# 1.create the struct asset
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
my_struct = asset_tools.create_asset("IAMStruct", "/Game/CreatedByPython", unreal.UserDefinedStruct, unreal.StructureFactory())
unreal.PythonStructLib.add_variable(my_struct, "bool", "", None, 0, False)
unreal.PythonStructLib.add_variable(my_struct, "struct", "", unreal.Transform.static_struct(), 0, False)
unreal.PythonStructLib.add_variable(my_struct, "object", "", unreal.StaticMesh.static_class(), 0, False)

# 2.remove the default bool variable
unreal.PythonStructLib.remove_variable_by_name(my_struct, unreal.PythonStructLib.get_variable_names(my_struct)[0])

# 3.rename the property_name in struct which also shows in datatable.
# This is a pool way, and will be replaced by PythonStructLib.add_variable in next version.
better_names = ["my_bool_var", "my_transform_var", "my_mesh_var"]
for i, property_name in enumerate(unreal.PythonStructLib.get_variable_names(my_struct)):
    guid = unreal.PythonStructLib.get_guid_from_property_name(property_name)
    unreal.PythonStructLib.rename_variable(my_struct, guid, better_names[i])

unreal.EditorAssetLibrary.save_asset("/Game/CreatedByPython/IAMStruct")



# 4.create the datatable asset
datatable_factory = unreal.DataTableFactory()
datatable_factory.struct = unreal.load_asset("/Game/CreatedByPython/IAMStruct.IAMStruct")
my_datatable = asset_tools.create_asset("IAmADataTable", "/Game/CreatedByPython", unreal.DataTable, datatable_factory)
unreal.EditorAssetLibrary.save_asset("/Game/CreatedByPython/IAmADataTable")


unreal.PythonDataTableLib.add_row(my_datatable, "row_1")
unreal.PythonDataTableLib.add_row(my_datatable, "row_2")

# 5.set the values in "row_1"
unreal.PythonDataTableLib.set_property_by_string(my_datatable, "row_1", "my_bool_var", "True")
unreal.PythonDataTableLib.set_property_by_string(my_datatable, "row_1", "my_transform_var"
                                                 , "(Rotation=(X=0,Y=0,Z=0,W=1),Translation=(X=1,Y=2,Z=3),Scale3D=(X=1.5,Y=1.5,Z=1.5))"
                                                 )
unreal.PythonDataTableLib.set_property_by_string(my_datatable, "row_1", "my_mesh_var"
                                                 , "StaticMesh'/Engine/Functions/Engine_MaterialFunctions02/SupportFiles/1x1x1_Box_Pivot_-XYZ.1x1x1_Box_Pivot_-XYZ'"
                                                 )
# 6.set the values in "row_2"
unreal.PythonDataTableLib.set_property_by_string_at(my_datatable, row_index=1, column_index=0, value_as_string="True")
unreal.PythonDataTableLib.set_property_by_string_at(my_datatable, row_index=1, column_index=1
                                                    , value_as_string="(Rotation=(X=0,Y=0,Z=0,W=1),Translation=(X=4,Y=5,Z=6),Scale3D=(X=3,Y=3,Z=3))"
                                                    )
unreal.PythonDataTableLib.set_property_by_string_at(my_datatable, row_index=1, column_index=2
                                                    , value_as_string="StaticMesh'/Engine/Functions/Engine_MaterialFunctions02/ExampleContent/TextureBasedWPO/DemoBoxMesh.DemoBoxMesh'")

unreal.EditorAssetLibrary.save_asset("/Game/CreatedByPython/IAmADataTable")