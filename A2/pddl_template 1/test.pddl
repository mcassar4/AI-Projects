(define (problem testproblem)
  (:domain Dungeon)
  (:objects
    loc-1-2 loc-2-2 - location
    key1 - k
    c1222 - corridor
  )

  (:init
    (hero-at loc-1-2)
    ; (not (hero-at loc-2-2))
    
    (cor-between loc-1-2 loc-2-2 c1222)
    ; (cor-between loc-2-2 loc-1-2 c1222)
  )
  
  (:goal
    (and
        (hero-at loc-2-2)
    )
  )
)
