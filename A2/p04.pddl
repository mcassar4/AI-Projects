(define (problem p4-dungeon)
  (:domain Dungeon)

  ; Come up with your own problem instance (see assignment for details)
  ; NOTE: You _may_ use new objects for this problem only.

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-1-1 loc-2-1 loc-3-1 loc-4-1 loc-5-1 loc-6-1 loc-7-1 - location
    c1121 c2131 c3141 c4151 c5161 c6171 - corridor
    key1 key2 key3 key4 key5 - k
  )

  (:init 
    ; hero starting location
    (hero-at loc-1-1)

    ; Corridor connections
    (cor-between loc-1-1 loc-2-1 c1121)
    (cor-between loc-2-1 loc-1-1 c1121)
    (cor-connected c1121 loc-1-1)
    (cor-connected c1121 loc-2-1)

    (cor-between loc-2-1 loc-3-1 c2131)
    (cor-between loc-3-1 loc-2-1 c2131)
    (cor-connected c2131 loc-2-1)
    (cor-connected c2131 loc-3-1)

    (cor-between loc-3-1 loc-4-1 c3141)
    (cor-between loc-4-1 loc-3-1 c3141)
    (cor-connected c3141 loc-3-1)
    (cor-connected c3141 loc-4-1)

    (cor-between loc-4-1 loc-5-1 c4151)
    (cor-between loc-5-1 loc-4-1 c4151)
    (cor-connected c4151 loc-4-1)
    (cor-connected c4151 loc-5-1)

    (cor-between loc-5-1 loc-6-1 c5161)
    (cor-between loc-6-1 loc-5-1 c5161)
    (cor-connected c5161 loc-5-1)
    (cor-connected c5161 loc-6-1)

    (cor-between loc-6-1 loc-7-1 c6171)
    (cor-between loc-7-1 loc-6-1 c6171)
    (cor-connected c6171 loc-6-1)
    (cor-connected c6171 loc-7-1)


    ; Locks
    (cor-locked c1121)
    (cor-lock-colour c1121 yellow)

    (cor-locked c2131)
    (cor-lock-colour c2131 yellow)

    (cor-locked c3141)
    (cor-lock-colour c3141 purple)

    (cor-locked c4151)
    (cor-lock-colour c4151 green)

    (cor-locked c5161)
    (cor-lock-colour c5161 red)

    (cor-locked c6171)
    (cor-lock-colour c6171 rainbow)


    ; Keys
    (key-colour key1 red)
    (key-at key1 loc-1-1)

    (key-two-use key2)
    (key-colour key2 yellow)
    (key-at key2 loc-1-1)

    (key-one-use key3)
    (key-colour key3 green)
    (key-at key3 loc-1-1)

    (key-one-use key4)
    (key-colour key4 purple)
    (key-at key4 loc-1-1)

    (key-one-use key5)
    (key-colour key5 rainbow)
    (key-at key5 loc-1-1)
  )
  (:goal
    (and
      ; Hero's final location goes here
      (hero-at loc-7-1)
    )
  )

)
