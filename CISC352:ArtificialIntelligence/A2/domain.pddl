(define (domain Dungeon)

    (:requirements
        :typing
        :negative-preconditions
        :conditional-effects
    )

    ; Do not modify the types
    (:types
        location colour k corridor
    )

    ; Do not modify the constants
    (:constants
        red yellow green purple rainbow - colour
    )

    ; You may introduce whatever predicates you would like to use
    (:predicates
        (hero-at ?loc - location)
        (key-at ?k - k ?loc - location)
        (holding-key ?k - k)
        (holding-any-key)

        (cor-between ?from ?to - location ?cor - corridor)
        (cor-connected ?cor - corridor ?loc - location)
        
        (key-colour ?k - k ?col - colour)
        (key-used ?k - k)

        (key-one-use ?k - k)
        (key-two-use ?k - k)

        (cor-locked ?cor - corridor)
        (cor-lock-colour ?cor - corridor ?col - colour)

        (cor-collapsed ?cor - corridor)

        (messy ?loc - location)
        (stash-key ?k - k)
    )

    ; IMPORTANT: You should not change/add/remove the action names or parameters

    ;Hero can move if the
    ;    - hero is at current location ?from,
    ;    - hero will move to location ?to,
    ;    - corridor ?cor - corridor exists between the ?from and ?to locations
    ;    - there isn't a locked door in corridor ?cor - corridor
    ;Effects move the hero, and collapse the corridor if it's "risky" (also causing a mess in the ?to location)
    (:action move

        :parameters (?from ?to - location ?cor - corridor)

        :precondition (and
            (hero-at ?from) ;hero is at current location from
            (cor-between ?from ?to ?cor) ;corridor exists between the from and to locations
            (not (cor-collapsed ?cor)) ; Collapsed corridors cant be used
            (not (cor-locked ?cor)) ; Locked corridors must be unlocked first
        )

        :effect (and
            (not (hero-at ?from))
            (hero-at ?to) ;move the hero
            ; if its risky:
            (when 
                (cor-lock-colour ?cor red) ;if
                (and ;then
                    (cor-collapsed ?cor)
                    (messy ?to)
                )
            )
        )
    )
    
    ;Hero can pick up a key if the
    ;    - hero is at current location ?loc - location,
    ;    - there is a key ?k - k at location ?loc - location,
    ;    - the hero's arm is free,
    ;    - the location is not messy
    ;Effect will have the hero holding the key and their arm no longer being free
    (:action pick-up

        :parameters (?loc - location ?k - k)

        :precondition (and
            (hero-at ?loc)
            (key-at ?k ?loc)
            ; cant be holding any key at all; not just the key in question
            (not (holding-any-key)); hero's arm is free
            (not (messy ?loc)) ; hero can only pickup if the room is clean
        )

        :effect (and
            (not (key-at ?k ?loc)) ; remove key from the room
            (holding-any-key) ; arm not free now
            (holding-key ?k) ; hero is holding the key 
        )
    )

    ;Hero can drop a key if the
    ;    - hero is holding a key ?k - k,
    ;    - the hero is at location ?loc - location
    ;Effect will be that the hero is no longer holding the key
    (:action drop

        :parameters (?loc - location ?k - k)

        :precondition (and
            (hero-at ?loc)
            (holding-any-key)
            (holding-key ?k)
        )

        :effect (and
            (not (holding-any-key))
            (not (holding-key ?k))
            (key-at ?k ?loc)
        )
    )


    ;Hero can use a key for a corridor if
    ;    - the hero is holding a key ?k - k,
    ;    - the key still has some uses left,
    ;    - the corridor ?cor - corridor is locked with colour ?col - colour,
    ;    - the key ?k - k is if the right colour ?col - colour,
    ;    - the hero is at location ?loc - location
    ;    - the corridor is connected to the location ?loc - location
    ;Effect will be that the corridor is unlocked and the key usage will be updated if necessary
    (:action unlock

        :parameters (?loc - location ?cor - corridor ?col - colour ?k - k)

        :precondition (and
            (hero-at ?loc) ; hero is at the location
            (not (messy ?loc)) ; from location isnt messy (clean it first)
            (holding-any-key) ; hero is holding a key
            (holding-key ?k) ; hero is holding the key
            (key-colour ?k ?col) ; The key that the hero is holding is the rought colour
            (not (key-used ?k)) ; The key has uses left
            (cor-locked ?cor) ; The specified corridor is locked
            (cor-lock-colour ?cor ?col) ; and its locked witht he right colour
            (cor-connected ?cor ?loc)  ;corridor is connected to location loc
        )

        :effect (and
            ; update key useage
            (when 
                (key-one-use ?k) ;if
                (and ;then the key is used up!
                    (not (key-one-use ?k)) ; use removed
                    (not (holding-any-key))
                    (not (holding-key ?k)) ; the hero isnt holding it anymore
                    (key-used ?k)
                    (stash-key ?k)
                )
            )
            (when 
                (key-two-use ?k) ;if
                (and ;then the key has only one use
                    (not (key-two-use ?k)) ; key no longer has 2 uses
                    (key-one-use ?k) ; updated key has only one use
                )
            )

            (not (cor-locked ?cor)) ; unlock the corridor regardless
        )
    )

    ;Hero can clean a location if
    ;    - the hero is at location ?loc - location,
    ;    - the location is messy
    ;Effect will be that the location is no longer messy
    (:action clean

        :parameters (?loc - location)

        :precondition (and
            (hero-at ?loc)
            (messy ?loc)
        )

        :effect (and
            (not (messy ?loc))
        )
    )
)