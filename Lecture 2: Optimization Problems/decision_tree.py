def decision_tree(to_consider, avail):
    if to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_cost() > avail:
        result = decision_tree(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        with_val, with_to_take = decision_tree(
            to_consider[1:], 
            avail - next_item.get_cost())
        
        with_val += next_item.get_value()

        without_val, without_to_take = decision_tree(
            to_consider[1:], avail
        )

        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    
    return result
