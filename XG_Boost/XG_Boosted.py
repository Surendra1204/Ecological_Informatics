import arcpy
arcpy.ImportToolbox(r"@\Spatial Statistics Tools.tbx")
arcpy.stats.Forest(
    prediction_type="PREDICT_RASTER",
    in_features="GTP_Final",
    variable_predict="Class",
    treat_variable_as_categorical="CATEGORICAL",
    explanatory_variables=None,
    distance_features=None,
    explanatory_rasters="Extract_Extr1 #;PCA2_Resample__CreatePanshar #",
    features_to_predict=None,
    output_features=None,
    output_raster=r"D:\University\Imam Turki bin Abdullah Royal Natural Reserve\EMIT\Final\Model\GB\GB_6\GB_6.tif",
    explanatory_variable_matching=None,
    explanatory_distance_matching=None,
    explanatory_rasters_matching="Extract_Extr1 Extract_Extr1;PCA2_Resample__CreatePanshar PCA2_Resample__CreatePanshar",
    output_trained_features=r"D:\University\Imam Turki bin Abdullah Royal Natural Reserve\EMIT\Final\Model\GB\GB_6\Output_Trained_Features_GB_6.shp",
    output_importance_table=r"D:\University\Imam Turki bin Abdullah Royal Natural Reserve\EMIT\Final\Model\GB\GB_6\Variable_Importance_GB_6.dbf",
    use_raster_values="TRUE",
    number_of_trees=10000,
    minimum_leaf_size=None,
    maximum_depth=None,
    sample_size=100,
    random_variables=None,
    percentage_for_training=15,
    output_classification_table=r"D:\University\Imam Turki bin Abdullah Royal Natural Reserve\EMIT\Final\Model\GB\GB_6\Confusion_Matrix_GB_6.dbf",
    output_validation_table=r"D:\University\Imam Turki bin Abdullah Royal Natural Reserve\EMIT\Final\Model\GB\GB_6\Validation_Table.dbf",
    compensate_sparse_categories="FALSE",
    number_validation_runs=3,
    calculate_uncertainty="FALSE",
    output_trained_model=r"D:\University\Imam Turki bin Abdullah Royal Natural Reserve\EMIT\Final\Model\GB\GB_6\GB_6.ssm",
    model_type="GRADIENT_BOOSTED",
    reg_lambda=1,
    gamma=0,
    eta=0.3,
    max_bins=0,
    optimize="FALSE",
    optimize_algorithm="",
    optimize_target="",
    num_search=None,
    model_param_setting=None,
    output_param_tuning_table=None,
    include_probabilities="HIGHEST_PROBABILITY_ONLY"
)
