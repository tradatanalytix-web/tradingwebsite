import opstrat as op


def ironbutterfly(strike1, pr1, strike2, pr2, strike3, pr3, strike4, pr4):

    op1={'op_type': 'c', 'strike': strike1, 'tr_type': 's', 'op_pr': pr1}
    op2={'op_type': 'c', 'strike': strike2, 'tr_type': 'b', 'op_pr': pr2}
    op3={'op_type': 'p', 'strike': strike3, 'tr_type': 's', 'op_pr': pr3}
    op4={'op_type': 'p', 'strike': strike4, 'tr_type': 'b', 'op_pr': pr4}

    op_list=[op1, op2, op3, op4]
    figib = op.multi_plotter(spot=17100,spot_range=50, op_list=op_list)

    return(figib)