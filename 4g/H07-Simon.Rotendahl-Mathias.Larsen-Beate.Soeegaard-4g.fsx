

(*4g.2*)
let a = [1; 2; 1; 3; 2]
let removeDuplicates a = 
    List.distinct a
//val removeDuplicates : a:'a list -> 'a list when 'a : equality
printf "%A\n" (removeDuplicates a)