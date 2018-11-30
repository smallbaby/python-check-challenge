#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author   :kaizhang01
# datetime :2018/11/24 下午8:11
# desc     :
'''

A
    a1 [1]
        a11 [2]
        a12 [2]
            a121 [3]
    b1 [1]
        b2 [2]
        b3 [2]
            b4 [3]
                b5 [4]
                b6 [4]
                b7 [4]
                b8 [4]
                    b9 [5]
                    b10 [6]
'''

data1 = {'A': ['a1', 'b1'],
         'a1': ['a11', 'a12'],
         'b1': ['b2', 'b3'],
         'b3': ['b4', 'b2'],
         'a12': ['a121'],
         'b4': ['b5', 'b6', 'a1', 'b7', 'b8'],
         'b8': ['b9', 'b10']
         }

data = {
    "dwd.dwd_loan_request_privilege_full": [
        "ods.biz_tb_loanrequest_privilege_full"
    ],
    "dwi.dwi_loan_base_full": [
        "dwi.dwi_loan_request_privilege_full"
    ],
    "dwi.dwi_loan_request_privilege_full": [
        "dwd.dwd_loan_request_privilege_full"
    ],
    "dwi.dwi_ordr_invest_full": [
        "dwi.dwi_loan_base_full"
    ],
    "dwi.dwi_ordr_overall_invest_full": [
        "dwi.dwi_ordr_invest_full"
    ],
    "dws.dws_user_base_full": [
        "dws.dws_user_ins_curr_full",
    ],
    "dws.dws_user_ins_curr_full": [
        "dwi.dwi_ordr_overall_invest_full"
    ],
    "dws.dws_user_summary_info_full": [
        "dws.dws_user_base_full"
    ],
    "ods.biz_tb_loanrequest_privilege_full": [
        "db_Biz_info.TB_LOANREQUEST_PRIVILEGE"
    ],

    "tmp.tmp_channel_user_summary_info": [
        "dws.dws_user_summary_info_full"
    ]
}

data = {
        "dim.dim_channel_cate_ad": [
            "dim.dim_channel_cate_cd",
            "dim.dim_channel_static_flow",
            "dwd.dwd_flow_dsp_cps_ad_position_full"
        ],
        "dim.dim_fund_dictionary_item_full": [
            "ods.ots_fw_dictionary_item_full"
        ],
        "dwd.dwd_finc_dsp_income_cost_count_full": [
            "ods.dsp_income_cost_count_full"
        ],
        "dwd.dwd_finc_fund_record_full": [],
        "dwd.dwd_finc_ins_curr_interest_his_full": [
            "ods.aztec_ins_interest_history_full"
        ],
        "dwd.dwd_finc_ins_curr_rebuy_full": [
            "ods.aztec_ins_rebuy_full"
        ],
        "dwd.dwd_finc_ins_curr_redeem_his_full": [
            "ods.aztec_ins_redeem_history_full"
        ],
        "dwd.dwd_finc_ins_interest_his_full": [
            "ods.insurance_ins_interest_history_full"
        ],
        "dwd.dwd_finc_ins_order_full": [
            "ods.insurance_ins_order_full"
        ],
        "dwd.dwd_finc_ins_redeem_his_full": [
            "ods.insurance_ins_redeem_history_full"
        ],
        "dwd.dwd_flow_dsp_cps_ad_position_full": [
            "ods.dsp_cps_ad_position_full"
        ],
        "dwd.dwd_loan_base_full": [
            "ods.biz_tb_loan_full"
        ],
        "dwd.dwd_loan_fund_full": [
            "ods.ots_pd_fund_full"
        ],
        "dwd.dwd_loan_repayment_full": [
            "ods.biz_tb_loan_repayment_full"
        ],
        "dwd.dwd_loan_request_bill_full": [
            "ods.biz_tb_loanrequest_bill_full"
        ],
        "dwd.dwd_loan_request_detail_full": [
            "ods.biz_tb_loanrequest_detail_full"
        ],
        "dwd.dwd_loan_request_fee_full": [
            "ods.biz_tb_loanrequest_fee_full"
        ],
        "dwd.dwd_loan_request_full": [
            "ods.biz_tb_loanrequest_full"
        ],
        "dwd.dwd_loan_request_privilege_full": [
            "ods.biz_tb_loanrequest_privilege_full"
        ],
        "dwd.dwd_loan_request_product_full": [
            "ods.biz_tb_loanrequest_product_full"
        ],
        "dwd.dwd_ordr_cash_invest_application_full": [
            "ods.goddess_td_invest_application_full"
        ],
        "dwd.dwd_ordr_dsp_cps_order_full": [
            "ods.dsp_cps_order_settle_full"
        ],
        "dwd.dwd_ordr_fund_cash_ordr_full": [
            "ods.fengfd_fc_order_full"
        ],
        "dwd.dwd_ordr_fund_trade_confirm_full": [
            "ods.ots_cl_trade_confirm_full"
        ],
        "dwd.dwd_ordr_fund_trade_request_full": [
            "ods.ots_tr_trade_request_full"
        ],
        "dwd.dwd_ordr_ins_order_annuity_renew_full": [
            "ods.ins_trade_ins_order_annuity_renew_full"
        ],
        "dwd.dwd_ordr_ins_order_applicant_full": [
            "ods.ins_trade_ins_order_applicant_full"
        ],
        "dwd.dwd_ordr_ins_order_full": [
            "dim.dim_common_address",
            "ods.ins_trade_ins_order_full"
        ],
        "dwd.dwd_ordr_ins_protect_car_buy_full": [
            "ods.ins_trade_td_car_order_full"
        ],
        "dwd.dwd_ordr_ins_protect_car_company_product_full": [
            "ods.ins_trade_tc_car_company_product_full"
        ],
        "dwd.dwd_ordr_ins_protect_car_policy_info_full": [
            "ods.ins_trade_td_car_order_policy_full"
        ],
        "dwd.dwd_ordr_ins_protect_order_buy_full": [
            "ods.ins_trade_ins_order_buy_full"
        ],
        "dwd.dwd_ordr_invest_full": [
            "ods.biz_tb_invest_full",
            "ods.biz_tb_order_full"
        ],
        "dwd.dwd_ordr_invest_p2p_detail_full": [
            "ods.asset_tb_combination_allot_full",
            "ods.asset_tb_invest_full",
            "ods.asset_tb_order_full",
            "ods.fengchu_tb_fund_allot_full"
        ],
        "dwd.dwd_ordr_us_stock_order_history_full": [
            "ods.stock_tab_trade_history_order_full"
        ],
        "dwd.dwd_user_base_full": [
            "dim.dim_comm_region_mobile",
            "dwd.dwd_user_base_full",
            "dwd.dwd_user_emp_full",
            "dwd.dwd_user_invalid_mobile",
            "ods.usercenter_tb_user_full"
        ],
        "dwd.dwd_user_corporation_user_full": [
            "ods.usercenter_tb_corporation_user_full"
        ],
        "dwd.dwd_user_corporation_user_maintain_full": [
            "ods.biz_tb_corporation_user_maintain_full"
        ],
        "dwd.dwd_user_emp_full": [
            "ods.oa_orguser_full"
        ],
        "dwd.dwd_user_fund_ta_account_full": [
            "ods.ots_ac_ta_account_full"
        ],
        "dwd.dwd_user_fund_user_full": [
            "ods.fengfd_fd_user_full"
        ],
        "dwd.dwd_user_ins_account_company_full": [
            "ods.ins_account_ins_company_full"
        ],
        "dwd.dwd_user_us_stock_account_full": [
            "ods.stock_tab_trade_account_full"
        ],
        "dwi.dwi_finc_record_full": [
            "dwd.dwd_finc_fund_record_full",
            "dwd.dwd_finc_ins_curr_interest_his_full",
            "dwd.dwd_finc_ins_curr_rebuy_full",
            "dwd.dwd_finc_ins_curr_redeem_his_full",
            "dwd.dwd_finc_ins_interest_his_full",
            "dwd.dwd_finc_ins_order_full",
            "dwd.dwd_finc_ins_redeem_his_full"
        ],
        "dwi.dwi_loan_base_full": [
            "dwd.dwd_loan_base_full",
            "dwd.dwd_loan_repayment_full",
            "dwd.dwd_loan_request_bill_full",
            "dwd.dwd_loan_request_detail_full",
            "dwd.dwd_loan_request_fee_full",
            "dwd.dwd_loan_request_full",
            "dwd.dwd_loan_request_product_full",
            "dwd.dwd_user_base_full",
            "dwd.dwd_user_corporation_user_full",
            "dwd.dwd_user_corporation_user_maintain_full",
            "dwi.dwi_loan_request_privilege_full"
        ],
        "dwi.dwi_loan_request_privilege_full": [
            "dwd.dwd_loan_request_privilege_full"
        ],
        "dwi.dwi_ordr_all_invest_full": [
            "dim.dim_user_base",
            "dwd.dwd_finc_dsp_income_cost_count_full",
            "dwi.dwi_loan_all_loan_full",
            "dwi.dwi_ordr_invest_fengchu_full",
            "dwi.dwi_ordr_invest_full",
            "dwi.dwi_ordr_invest_p2p_detail_full",
            "dwi.dwi_ordr_invest_p2p_full"
        ],
        "dwi.dwi_ordr_fund_full": [
            "dim.dim_fund_dictionary_item_full",
            "dwd.dwd_loan_fund_full",
            "dwd.dwd_ordr_fund_cash_ordr_full",
            "dwd.dwd_ordr_fund_trade_confirm_full",
            "dwd.dwd_ordr_fund_trade_request_full",
            "dwd.dwd_user_fund_ta_account_full",
            "dwd.dwd_user_fund_user_full"
        ],
        "dwi.dwi_ordr_ins_protect_order_buy_full": [
            "dim.dim_channel_cate_ad",
            "dim.dim_common_ins_archives_data",
            "dim.dim_user_base",
            "dwd.dwd_ordr_dsp_cps_order_full",
            "dwd.dwd_ordr_ins_order_annuity_renew_full",
            "dwd.dwd_ordr_ins_order_applicant_full",
            "dwd.dwd_ordr_ins_order_full",
            "dwd.dwd_ordr_ins_protect_car_buy_full",
            "dwd.dwd_ordr_ins_protect_car_company_product_full",
            "dwd.dwd_ordr_ins_protect_car_policy_info_full",
            "dwd.dwd_ordr_ins_protect_order_buy_full",
            "dwd.dwd_user_ins_account_company_full"
        ],
        "dwi.dwi_ordr_invest_cash_full": [
            "dim.dim_channel_cate_cd",
            "dim.dim_user_base",
            "dwd.dwd_ordr_cash_invest_application_full"
        ],
        "dwi.dwi_ordr_invest_full": [
            "dim.dim_channel_cate_ad",
            "dim.dim_comm_channel",
            "dim.dim_user_base",
            "dwd.dwd_ordr_dsp_cps_order_full",
            "dwd.dwd_ordr_invest_full",
            "dwi.dwi_loan_base_full"
        ],
        "dwi.dwi_ordr_invest_p2p_detail_full": [
            "dim.dim_channel_cate_ad",
            "dim.dim_comm_channel",
            "dim.dim_user_base",
            "dwd.dwd_ordr_dsp_cps_order_full",
            "dwd.dwd_ordr_invest_p2p_detail_full",
            "dwi.dwi_loan_base_p2p_full",
            "dwi.dwi_ordr_invest_p2p_full"
        ],
        "dwi.dwi_ordr_invest_p2p_full": [
            "dim.dim_channel_cate_ad",
            "dim.dim_comm_channel",
            "dim.dim_user_base",
            "dwd.dwd_ordr_dsp_cps_order_full",
            "dwd.dwd_ordr_invest_p2p_full",
            "dwi.dwi_loan_all_loan_full"
        ],
        "dwi.dwi_ordr_overall_invest_full": [
            "dim.dim_user_base",
            "dwd.dwd_finc_dsp_income_cost_count_full",
            "dwd.dwd_finc_ins_curr_rebuy_full",
            "dwi.dwi_loan_base_full",
            "dwi.dwi_ordr_invest_full"
        ],
        "dwi.dwi_ordr_us_stock_order_history_full": [
            "dwd.dwd_ordr_us_stock_order_history_full",
            "dwd.dwd_user_us_stock_account_full"
        ],
        "dwi.dwi_user_unique_channel_score_new_full": [
            "dim.dim_channel_cate_cd",
            "dwi.dwi_user_unique_channel_score_new"
        ],
        "dws.dws_user_base_full": [
            "dim.dim_user_base",
            "dwi.dwi_ordr_all_invest_full",
            "dws.dws_user_ins_curr_full",
            "dws.dws_user_invest_full",
            "dws.dws_user_makt_points_full",
            "dws.dws_user_profit_full",
            "dws.dws_user_recharge_withdraw_full"
        ],
        "dws.dws_user_channel_summary_info_full": [
            "dim.dim_user_base",
            "dwi.dwi_user_unique_channel_score_new_full",
            "dws.dws_user_summary_info_full"
        ],
        "dws.dws_user_ins_curr_full": [
            "dim.dim_user_base",
            "dwd.dwd_finc_ins_curr_interest_his_full",
            "dwi.dwi_ordr_overall_invest_full"
        ],
        "dws.dws_user_invest_full": [
            "dim.dim_channel_cate_cd",
            "dim.dim_user_base",
            "dwd.dwd_finc_ins_order_full",
            "dwi.dwi_loan_base_full",
            "dwi.dwi_ordr_all_invest_full",
            "dwi.dwi_ordr_fund_full",
            "dwi.dwi_ordr_ins_protect_order_buy_full",
            "dwi.dwi_ordr_invest_cash_full",
            "dwi.dwi_ordr_invest_full",
            "dwi.dwi_ordr_us_stock_order_history_full"
        ],
        "dws.dws_user_profit_full": [
            "dim.dim_user_base",
            "dwd.dwd_finc_fund_full",
            "dwi.dwi_ordr_invest_all_repay_full"
        ],
        "dws.dws_user_recharge_withdraw_full": [
            "dim.dim_user_base",
            "dwi.dwi_finc_record_full"
        ],
        "dws.dws_user_summary_info_full": [
            "dim.dim_user_base",
            "dwd.dwd_finc_fund_full",
            "dwi.dwi_finc_record_full",
            "dwi.dwi_ordr_all_invest_full",
            "dwi.dwi_ordr_invest_all_repay_full",
            "dws.dws_user_base_full"
        ],
        "ods.asset_tb_combination_allot_full": [
            "db_asset_info.TB_COMBINATION_ALLOT"
        ],
        "ods.asset_tb_invest_full": [
            "db_asset_info.TB_INVEST"
        ],
        "ods.asset_tb_order_full": [
            "db_asset_info.TB_ORDER"
        ],
        "ods.aztec_ins_interest_history_full": [
            "db_aztec_info.ins_interest_history"
        ],
        "ods.aztec_ins_rebuy_full": [
            "db_aztec_info.ins_rebuy"
        ],
        "ods.aztec_ins_redeem_history_full": [
            "db_aztec_info.ins_redeem_history"
        ],
        "ods.biz_tb_corporation_user_maintain_full": [
            "db_Biz_info.TB_CORPORATION_USER_MAINTAIN"
        ],
        "ods.biz_tb_invest_full": [
            "db_Biz_info.TB_INVEST"
        ],
        "ods.biz_tb_loan_full": [
            "db_Biz_info.TB_LOAN"
        ],
        "ods.biz_tb_loan_repayment_full": [
            "db_Biz_info.TB_LOAN_REPAYMENT"
        ],
        "ods.biz_tb_loanrequest_bill_full": [
            "db_Biz_info.TB_LOANREQUEST_BILL"
        ],
        "ods.biz_tb_loanrequest_detail_full": [
            "db_Biz_info.TB_LOANREQUEST_DETAIL"
        ],
        "ods.biz_tb_loanrequest_fee_full": [
            "db_Biz_info.TB_LOANREQUEST_FEE"
        ],
        "ods.biz_tb_loanrequest_full": [
            "db_Biz_info.TB_LOANREQUEST"
        ],
        "ods.biz_tb_loanrequest_privilege_full": [
            "db_Biz_info.TB_LOANREQUEST_PRIVILEGE"
        ],
        "ods.biz_tb_loanrequest_product_full": [
            "db_Biz_info.TB_LOANREQUEST_PRODUCT"
        ],
        "ods.biz_tb_order_full": [
            "db_Biz_info.TB_ORDER"
        ],
        "ods.dsp_cps_ad_position_full": [
            "db_dsp_info.cps_ad_position"
        ],
        "ods.dsp_cps_order_settle_full": [
            "db_dsp_info.cps_order_settle"
        ],
        "ods.dsp_income_cost_count_full": [
            "db_dsp_info.income_cost_count"
        ],
        "ods.fengchu_tb_fund_allot_full": [
            "db_fengchu_info.TB_FUND_ALLOT"
        ],
        "ods.fengfd_fc_order_full": [
            "db_fengfd_info.fc_order"
        ],
        "ods.fengfd_fd_user_full": [
            "db_fengfd_info.fd_user"
        ],
        "ods.fund_record_0_tb_fund_record_0_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_0"
        ],
        "ods.fund_record_0_tb_fund_record_1_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_1"
        ],
        "ods.fund_record_0_tb_fund_record_2_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_2"
        ],
        "ods.fund_record_0_tb_fund_record_3_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_3"
        ],
        "ods.fund_record_0_tb_fund_record_4_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_4"
        ],
        "ods.fund_record_0_tb_fund_record_5_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_5"
        ],
        "ods.fund_record_0_tb_fund_record_6_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_6"
        ],
        "ods.fund_record_0_tb_fund_record_7_full": [
            "db_fund_record_0_info.TB_FUND_RECORD_7"
        ],
        "ods.fund_record_1_tb_fund_record_0_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_0"
        ],
        "ods.fund_record_1_tb_fund_record_1_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_1"
        ],
        "ods.fund_record_1_tb_fund_record_2_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_2"
        ],
        "ods.fund_record_1_tb_fund_record_3_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_3"
        ],
        "ods.fund_record_1_tb_fund_record_4_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_4"
        ],
        "ods.fund_record_1_tb_fund_record_5_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_5"
        ],
        "ods.fund_record_1_tb_fund_record_6_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_6"
        ],
        "ods.fund_record_1_tb_fund_record_7_full": [
            "db_fund_record_1_info.TB_FUND_RECORD_7"
        ],
        "ods.goddess_td_invest_application_full": [
            "db_goddess_info.TD_INVEST_APPLICATION"
        ],
        "ods.ins_account_ins_company_full": [
            "db_ins_account_info.ins_company"
        ],
        "ods.ins_trade_ins_order_annuity_renew_full": [
            "db_ins_trade_info.ins_order_annuity_renew"
        ],
        "ods.ins_trade_ins_order_applicant_full": [
            "db_ins_trade_info.ins_order_applicant"
        ],
        "ods.ins_trade_ins_order_buy_full": [
            "db_ins_trade_info.ins_order_buy"
        ],
        "ods.ins_trade_ins_order_full": [
            "db_ins_trade_info.ins_order"
        ],
        "ods.ins_trade_tc_car_company_product_full": [
            "db_ins_trade_info.TC_CAR_COMPANY_PRODUCT"
        ],
        "ods.ins_trade_td_car_order_full": [
            "db_ins_trade_info.TD_CAR_ORDER"
        ],
        "ods.ins_trade_td_car_order_policy_full": [
            "db_ins_trade_info.TD_CAR_ORDER_POLICY"
        ],
        "ods.insurance_ins_interest_history_full": [
            "db_insurance_info.ins_interest_history"
        ],
        "ods.insurance_ins_order_full": [
            "db_insurance_info.ins_order"
        ],
        "ods.insurance_ins_redeem_history_full": [
            "db_insurance_info.ins_redeem_history"
        ],
        "ods.ots_ac_ta_account_full": [
            "db_OTS_info.AC_TA_ACCOUNT"
        ],
        "ods.ots_cl_trade_confirm_full": [
            "db_OTS_info.CL_TRADE_CONFIRM"
        ],
        "ods.ots_fw_dictionary_item_full": [
            "db_OTS_info.FW_DICTIONARY_ITEM"
        ],
        "ods.ots_pd_fund_full": [
            "db_OTS_info.PD_FUND"
        ],
        "ods.ots_tr_trade_request_full": [
            "db_OTS_info.TR_TRADE_REQUEST"
        ],
        "ods.stock_tab_trade_history_order_full": [
            "db_stock_info.TAB_TRADE_HISTORY_ORDER"
        ],
        "ods.usercenter_tb_corporation_user_full": [
            "db_usercenter_info.TB_CORPORATION_USER"
        ],
        "ods.usercenter_tb_user_full": [
            "db_usercenter_info.TB_USER"
        ],
        "tmp.tmp_channel_user_summary_info": [
            "dim.dim_channel_cate_cd",
            "dws.dws_user_channel_summary_info_full",
            "dws.dws_user_summary_info_full"
        ],
    "table": "tmp.tmp_channel_user_summary_info"
}


def parse(output, inputs):
    i = 0
    ids = {}
    used = inputs.copy()
    while inputs:
        node = inputs.pop()
        if node in ids:
            i = ids[node] + 1
        else:
            i += 1

        if node in data:
            print(node, i)
            for _n in data[node]:
                if _n not in used:
                    # print('----', node, _n, used)
                    used.append(_n)
                    ids[_n] = i
                    inputs.append(_n)
                    # print(ids)
        else:
            print(node, i)
            i = 0


if __name__ == '__main__':
    key = 'tmp.tmp_channel_user_summary_info'
    parse(key, data[key])
