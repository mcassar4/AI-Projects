(define (problem p3-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-3-4 loc-4-5 loc-1-2 loc-2-2 loc-3-2 loc-3-3 loc-2-5 loc-1-3 loc-2-1 loc-1-4 loc-3-5 loc-2-4 loc-4-4 loc-2-3 loc-4-3 - location
    c2122 c1222 c2232 c1213 c1223 c2223 c3223 c3233 c1323 c2333 c1314 c2314 c2324 c2334 c3334 c1424 c2434 c2425 c2535 c3545 c4544 c4443 - corridor
    key1 key2 key3 key4 key5 key6 - k
  )

  (:init
    ; hero starting location
    (hero-at loc-2-1)

    ; Corridor connections
    (cor-between loc-2-1 loc-2-2 c2122)
    (cor-between loc-2-2 loc-2-1 c2122)
    (cor-connected c2122 loc-2-1)
    (cor-connected c2122 loc-2-2)

    (cor-between loc-1-2 loc-2-2 c1222)
    (cor-between loc-2-2 loc-1-2 c1222)
    (cor-connected c1222 loc-1-2)
    (cor-connected c1222 loc-2-2)

    (cor-between loc-2-2 loc-3-2 c2232)
    (cor-between loc-3-2 loc-2-2 c2232)
    (cor-connected c2232 loc-2-2)
    (cor-connected c2232 loc-3-2)

    (cor-between loc-1-2 loc-1-3 c1213)
    (cor-between loc-1-3 loc-1-2 c1213)
    (cor-connected c1213 loc-1-2)
    (cor-connected c1213 loc-1-3)

    (cor-between loc-1-2 loc-2-3 c1223)
    (cor-between loc-2-3 loc-1-2 c1223)
    (cor-connected c1223 loc-1-2)
    (cor-connected c1223 loc-2-3)

    (cor-between loc-2-2 loc-2-3 c2223)
    (cor-between loc-2-3 loc-2-2 c2223)
    (cor-connected c2223 loc-2-2)
    (cor-connected c2223 loc-2-3)

    (cor-between loc-3-2 loc-2-3 c3223)
    (cor-between loc-2-3 loc-3-2 c3223)
    (cor-connected c3223 loc-3-2)
    (cor-connected c3223 loc-2-3)

    (cor-between loc-3-2 loc-3-3 c3233)
    (cor-between loc-3-3 loc-3-2 c3233)
    (cor-connected c3233 loc-3-2)
    (cor-connected c3233 loc-3-3)

    (cor-between loc-1-3 loc-2-3 c1323)
    (cor-between loc-2-3 loc-1-3 c1323)
    (cor-connected c1323 loc-1-3)
    (cor-connected c1323 loc-2-3)

    (cor-between loc-2-3 loc-3-3 c2333)
    (cor-between loc-3-3 loc-2-3 c2333)
    (cor-connected c2333 loc-2-3)
    (cor-connected c2333 loc-3-3)

    (cor-between loc-1-3 loc-1-4 c1314)
    (cor-between loc-1-4 loc-1-3 c1314)
    (cor-connected c1314 loc-1-3)
    (cor-connected c1314 loc-1-4)

    (cor-between loc-2-3 loc-1-4 c2314)
    (cor-between loc-1-4 loc-2-3 c2314)
    (cor-connected c2314 loc-2-3)
    (cor-connected c2314 loc-1-4)

    (cor-between loc-2-3 loc-2-4 c2324)
    (cor-between loc-2-4 loc-2-3 c2324)
    (cor-connected c2324 loc-2-3)
    (cor-connected c2324 loc-2-4)

    (cor-between loc-2-3 loc-3-4 c2334)
    (cor-between loc-3-4 loc-2-3 c2334)
    (cor-connected c2334 loc-2-3)
    (cor-connected c2334 loc-3-4)

    (cor-between loc-3-3 loc-3-4 c3334)
    (cor-between loc-3-4 loc-3-3 c3334)
    (cor-connected c3334 loc-3-3)
    (cor-connected c3334 loc-3-4)

    (cor-between loc-1-4 loc-2-4 c1424)
    (cor-between loc-2-4 loc-1-4 c1424)
    (cor-connected c1424 loc-1-4)
    (cor-connected c1424 loc-2-4)

    (cor-between loc-2-4 loc-3-4 c2434)
    (cor-between loc-3-4 loc-2-4 c2434)
    (cor-connected c2434 loc-2-4)
    (cor-connected c2434 loc-3-4)

    (cor-between loc-2-4 loc-2-5 c2425)
    (cor-between loc-2-5 loc-2-4 c2425)
    (cor-connected c2425 loc-2-4)
    (cor-connected c2425 loc-2-5)

    (cor-between loc-2-5 loc-3-5 c2535)
    (cor-between loc-3-5 loc-2-5 c2535)
    (cor-connected c2535 loc-2-5)
    (cor-connected c2535 loc-3-5)

    (cor-between loc-3-5 loc-4-5 c3545)
    (cor-between loc-4-5 loc-3-5 c3545)
    (cor-connected c3545 loc-3-5)
    (cor-connected c3545 loc-4-5)

    (cor-between loc-4-5 loc-4-4 c4544)
    (cor-between loc-4-4 loc-4-5 c4544)
    (cor-connected c4544 loc-4-5)
    (cor-connected c4544 loc-4-4)

    (cor-between loc-4-4 loc-4-3 c4443)
    (cor-between loc-4-3 loc-4-4 c4443)
    (cor-connected c4443 loc-4-4)
    (cor-connected c4443 loc-4-3)


    ; Locks
    (cor-locked c1223)
    (cor-lock-colour c1223 red)

    (cor-locked c2223)
    (cor-lock-colour c2223 red)

    (cor-locked c3223)
    (cor-lock-colour c3223 red)

    (cor-locked c1323)
    (cor-lock-colour c1323 red)

    (cor-locked c2333)
    (cor-lock-colour c2333 red)

    (cor-locked c2314)
    (cor-lock-colour c2314 red)

    (cor-locked c2324)
    (cor-lock-colour c2324 red)

    (cor-locked c2334)
    (cor-lock-colour c2334 red)

    (cor-locked c2535)
    (cor-lock-colour c2535 green)

    (cor-locked c4544)
    (cor-lock-colour c4544 green)

    (cor-locked c2425)
    (cor-lock-colour c2425 purple)

    (cor-locked c3545)
    (cor-lock-colour c3545 purple)

    (cor-locked c4443)
    (cor-lock-colour c4443 rainbow)


    ; Keys
    (key-colour key1 red)
    (key-at key1 loc-2-1)

    (key-one-use key2)
    (key-colour key2 green)
    (key-at key2 loc-2-3)

    (key-one-use key3)
    (key-colour key3 green)
    (key-at key3 loc-2-3)

    (key-one-use key4)
    (key-colour key4 purple)
    (key-at key4 loc-2-3)

    (key-one-use key5)
    (key-colour key5 purple)
    (key-at key5 loc-2-3)

    (key-one-use key6)
    (key-colour key6 rainbow)
    (key-at key6 loc-4-4)
  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-4-3)
    )
  )

)
