(define (problem p1-dungeon)
  (:domain Dungeon)
  (:objects
    loc-3-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 loc-3-3 loc-2-4 loc-3-4 loc-4-4 - location
    key1 key2 key3 key4 - k
    c3132 c1222 c2232 c3242 c2223 c3233 c2333 c2324 c3334 c2434 c3444 - corridor
  )

  (:init
    ; hero starting location
    (hero-at loc-1-2)

    ; Corridor connections
    (cor-between loc-3-1 loc-3-2 c3132)
    (cor-between loc-3-2 loc-3-1 c3132)
    (cor-connected c3132 loc-3-1)
    (cor-connected c3132 loc-3-2)

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

    (cor-between loc-3-2 loc-3-3 c3233)
    (cor-between loc-3-3 loc-3-2 c3233)
    (cor-connected c3233 loc-3-2)
    (cor-connected c3233 loc-3-3)

    (cor-between loc-2-3 loc-3-3 c2333)
    (cor-between loc-3-3 loc-2-3 c2333)
    (cor-connected c2333 loc-2-3)
    (cor-connected c2333 loc-3-3)

    (cor-between loc-2-3 loc-2-4 c2324)
    (cor-between loc-2-4 loc-2-3 c2324)
    (cor-connected c2324 loc-2-3)
    (cor-connected c2324 loc-2-4)

    (cor-between loc-3-3 loc-3-4 c3334)
    (cor-between loc-3-4 loc-3-3 c3334)
    (cor-connected c3334 loc-3-3)
    (cor-connected c3334 loc-3-4)

    (cor-between loc-2-4 loc-3-4 c2434)
    (cor-between loc-3-4 loc-2-4 c2434)
    (cor-connected c2434 loc-2-4)
    (cor-connected c2434 loc-3-4)

    (cor-between loc-3-4 loc-4-4 c3444)
    (cor-between loc-4-4 loc-3-4 c3444)
    (cor-connected c3444 loc-3-4)
    (cor-connected c3444 loc-4-4)


    ; Locks
    (cor-locked c3132)
    (cor-lock-colour c3132 rainbow)

    (cor-locked c3242)
    (cor-lock-colour c3242 purple)

    (cor-locked c2324)
    (cor-lock-colour c2324 red)

    (cor-locked c2434)
    (cor-lock-colour c2434 red)

    (cor-locked c3444)
    (cor-lock-colour c3444 yellow)


    ; Keys
    (key-colour key1 red)
    (key-at key1 loc-2-2)

    (key-two-use key2)
    (key-colour key2 yellow)
    (key-at key2 loc-2-4)

    (key-one-use key4)
    (key-colour key4 purple)
    (key-at key4 loc-4-4)

    (key-one-use key3)
    (key-colour key3 rainbow)
    (key-at key3 loc-4-2)
  )
  
  (:goal
    (and
        (hero-at loc-3-1)
    )
  )
)
