
let a = [1;1;2]
let b = [1;2;4]
let c = [1;1;1;2;2]
let d = [1;1;2;3]

//4.11-4
(*
this function returns an ordered list that is combination of two list. 
*)
let plus x xs = x @ xs |> List.sort
printf "%A\n" (plus a b)
printf "%s\n" "*******************"


//4.11-5 :: works for d - c 
(*
this function returns an list, where the elements are obtained by removing 
the elemtents that are also found in the second list from the first list. 
    *)
let minus x xs = (Set.ofList x) - (Set.ofList xs) |> Set.toList
//let minus x xs = x |> List.filter (fun i -> not (List.contains i xs))
printf "%A\n" (minus c d)