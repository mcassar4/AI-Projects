(define (problem p2-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-2-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 - location
    key1 key2 key3 key4 - k
    c2122 c1222 c2232 c3242 c2223 - corridor
  )

  (:init
    ; hero starting location
    (hero-at loc-2-2)

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

    (cor-between loc-3-2 loc-4-2 c3242)
    (cor-between loc-4-2 loc-3-2 c3242)
    (cor-connected c3242 loc-3-2)
    (cor-connected c3242 loc-4-2)

    (cor-between loc-2-2 loc-2-3 c2223)
    (cor-between loc-2-3 loc-2-2 c2223)
    (cor-connected c2223 loc-2-2)
    (cor-connected c2223 loc-2-3)

   ; Locks
    (cor-locked c2122)
    (cor-lock-colour c2122 purple)

    (cor-locked c1222)
    (cor-lock-colour c1222 yellow)

    (cor-locked c2232)
    (cor-lock-colour c2232 yellow)

    (cor-locked c3242)
    (cor-lock-colour c3242 rainbow)

    (cor-locked c2223)
    (cor-lock-colour c2223 green)


    ; Keys
    (key-one-use key1)
    (key-colour key1 green)
    (key-at key1 loc-2-1)

    (key-one-use key2)
    (key-colour key2 rainbow)
    (key-at key2 loc-1-2)

    (key-one-use key3)
    (key-colour key3 purple)
    (key-at key3 loc-2-2)

    (key-two-use key4)
    (key-colour key4 yellow)
    (key-at key4 loc-2-3)
  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-4-2)
    )
  )

)
