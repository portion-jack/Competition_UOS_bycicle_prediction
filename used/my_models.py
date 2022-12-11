kernel_ridge=KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5)
# gradient_boosting=GradientBoostingRegressor()

gradient_boosting = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=4, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10,
                                   loss='huber', random_state =5)

model_xgb = XGBRegressor(colsample_bytree=0.4603, gamma=0.0468,
                             learning_rate=0.05, max_depth=3,
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)

model_lgb = LGBMRegressor(objective='regression',num_leaves=5,
                              learning_rate=0.05, n_estimators=2200,
                              max_bin = 55, bagging_fraction = 0.8,
                              bagging_freq = 5, feature_fraction = 0.2319,
                              feature_fraction_seed=9, bagging_seed=9,
                              min_data_in_leaf =6, min_sum_hessian_in_leaf = 11)


vot_model3 = VotingRegressor(
    [('m1',kernel_ridge),
     ('m2',model_xgb),
     ('m3',model_lgb),
     ('m4',gradient_boosting)]
)


vot_model1 = VotingRegressor(
    [('m1',kernel_ridge),
     ('m2',model_xgb),
     ('m3',model_lgb),
     ('m4',gradient_boosting)]
)
vot_model2 = VotingRegressor(
    [('m1',kernel_ridge),
     ('m2',model_xgb),
     ('m3',model_lgb),
     ('m4',gradient_boosting)]
)
vot_model3 = VotingRegressor(
    [('m1',kernel_ridge),
     ('m2',model_xgb),
     ('m3',model_lgb),
     ('m4',gradient_boosting)]
)
vot_model4 = VotingRegressor(
    [('m1',kernel_ridge),
     ('m2',model_xgb),
     ('m3',model_lgb),
     ('m4',gradient_boosting)]
)
