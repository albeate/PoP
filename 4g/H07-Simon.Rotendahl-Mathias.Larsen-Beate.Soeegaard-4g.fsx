///////////4.11/////////////
//1.
let count x xs =
    match (List.countBy (fun elem -> elem = x) xs) with
    | [(true,n);_] -> n
    | _ -> -1

//2.
let mutable x = 5
let mutable xs = [1;2;3;4;6;7;8;9]
let insert (L : int list * int) =
    let (xs,x) = L
    let mutable i = 0
    while xs.[i] < x && i < xs.Length do
        i <- i + 1
    if x < xs.[i] then
        xs.[..i-1] @ [x] @ xs.[i..]
    else
        xs @ [x]
printf "%A" (insert (xs,x))

//3.
let intersect (a : int list * int list) =
    let mutable (xs,ys) = a
    let mutable zs = []
    while xs.Length <> 0 && ys.Length <> 0 do
        match (xs, ys) with
        | (x :: xss, y :: yss)->
            if (x = y) then
                zs <- zs @ [x]
                xs <- xss
                ys <- yss
            elif (x < y) then xs <- xss
            elif (y < x) then ys <- yss
        | _ -> failwith ("matching went wrong.")
    zs

//4.
(*
this function returns an ordered list that is combination of two list. 
*)
let plus x xs = x @ xs |> List.sort
printf "%A\n" (plus a b)
printf "%s\n" "*******************"


//5. 
let rec minus lsx lsy = 
    match (lsx,lsy) with 
    | (x :: xs, y :: ys) ->
        if x < y then
            x :: (minus xs lsy)
        elif x > y then 
            minus lsx ys
        else 
            minus xs ys
    | (xs,_) -> xs 
    


///////////4.15/////////////
let revrev (a : 'T list list) =
    List.rev a |> List.map (fun elm -> List.rev elm) 



///////////4g.2/////////////
let removeDuplicates a = List.distinct a
