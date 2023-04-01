(define (problem testProblem)
  (:domain Dungeon)
  (:objects
    loc-1-2 loc-2-2 loc-3-2 loc-3-1 - location
    key1 key2 - k
    c1222 c2232 c3132 - corridor
  )

  (:init
    ; hero starting location
    (hero-at loc-1-2)

    ; Corridor connections
    (cor-between loc-1-2 loc-2-2 c1222)
    (cor-between loc-2-2 loc-1-2 c1222)
    (cor-connected c1222 loc-1-2)
    (cor-connected c1222 loc-2-2)

    (cor-between loc-2-2 loc-3-2 c2232)
    (cor-between loc-3-2 loc-2-2 c2232)
    (cor-connected c2232 loc-2-2)
    (cor-connected c2232 loc-3-2)

    (cor-between loc-3-1 loc-3-2 c3132)
    (cor-between loc-3-2 loc-3-1 c3132)
    (cor-connected c3132 loc-3-1)
    (cor-connected c3132 loc-3-2)
    

    ; Locks
    (cor-locked c2232)
    (cor-lock-colour c2232 red)

    (cor-locked c3132)
    (cor-lock-colour c3132 yellow)

    ; Keys
    ; (key-multi-use key1) ; how many uses the key starts with (unnecessary for red keys)
    (key-colour key1 red) ; what colour is the key
    (key-at key1 loc-2-2) ; where is the key

    ; (key-multi-use key2) ; how many uses the key starts with (unnecessary for red keys)
    (key-colour key2 yellow) ; what colour is the key
    (key-at key2 loc-3-2) ; where is the key
  )
  
  (:goal
    (and
        (hero-at loc-3-1)
    )
  )
)
