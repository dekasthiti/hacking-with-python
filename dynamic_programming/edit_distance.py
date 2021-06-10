def edit_distance_impl(s1, s2, edit_dist):
    s2_len = len(s2)
    s1_len = len(s1)
    print(f"{s1}")
    print(f"{s2}")
   
    if s2_len and s1_len:
        for i in range(s2_len):
            if s1[i] == s2[i]:
                if s1_len > i + 1:
                    print(f"Edit dist from 11: {edit_dist}\n")
                    return edit_distance_impl(s1[i+1:], s2[i+1:], edit_dist)
                else:
                    edit_dist += (s2_len - 1) # Remaining letters of s2 will need to be added
                    break
            else:
                edit_dist += 1
                print(f"Edit dist from 18: {edit_dist}\n")
                return edit_distance_impl(s1[i:], s2[i+1:], edit_dist)
    elif s2_len:
        edit_dist += (s2_len)
        print(f"Edit dist from 22: {edit_dist}\n")
    elif s1_len:
        edit_dist += (s1_len)  # Remaining letters of s1 will need to be removed.
        print(f"Edit dist from 25: {edit_dist}\n")

    print(f"Edit dist: {edit_dist}\n")
    return edit_dist


# cost[s1[i], s2[j]] = cost[s1[i+1]], s2[[j + 1]] if s1[i] == s2[j]
# or,
# min(add_cost(), replace_cost(), remove_cost())

# add_cost(s1[i], s2[j]): 1 + cost(s1[i], s2[j+1])

# replace_cost(s1[i], s2[j]) = 1 + cost(s1[i+1], s2[j+1])
# remove_cost(s1[i], s2[j]) = 1 + cost(s1[i+1], s2[j])

ADD_COST = 1
REMOVE_COST = 1
REPLACE_COST = 1


def cost(editable_str, source_str, editable_idx, source_idx):
    if editable_idx < len(editable_str):
        if source_idx < len(source_str):
            if editable_str[editable_idx] == source_str[source_idx]:
                return cost(editable_str, source_str, editable_idx + 1, source_idx + 1)
            else:
                return min(ADD_COST + cost(editable_str, source_str, editable_idx, source_idx + 1),
                           REPLACE_COST + cost(editable_str, source_str, editable_idx + 1, source_idx + 1),
                           REMOVE_COST + cost(editable_str, source_str, editable_idx + 1, source_idx))
        else:
            # Add what's left of editable string (we'll remove these letters)
            return len(editable_str) - editable_idx
    else:
        # Add what's left of the source string (we'll add these letters)
        return len(source_str) - source_idx
    
        
    
    
def edit_distance(s1, s2):
    
    if not s1:
        # Destination is None, add all the letters of the source
        return len(s2)
    elif not s2:
        # Source is None, delete all the letters of destination
        return len(s1)
    else:
        # edit_dist = edit_distance_impl(s1, s2, 0)
        edit_dist = cost(s1, s2, 0, 0)
        return edit_dist
       
        
if __name__ == '__main__':
    s1 = input("Enter string1: ")
    s2 = input("Enter string2: ")
    edit_dist = edit_distance(s1, s2)
    print(f"Edit distance between {s1} and {s2} is: {edit_dist}")