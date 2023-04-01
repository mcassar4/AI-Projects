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
        (cor-between ?from ?to - location ?cor - corridor)
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
        )

        :effect (and
            ; (not (hero-at ?from))
            (hero-at ?to) ;move the hero
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
            ; IMPLEMENT
        )

        :effect (and
            ; IMPLEMENT
        )
    )

    ;Hero can drop a key if the
    ;    - hero is holding a key ?k - k,
    ;    - the hero is at location ?loc - location
    ;Effect will be that the hero is no longer holding the key
    (:action drop

        :parameters (?loc - location ?k - k)

        :precondition (and
            ; IMPLEMENT
        )

        :effect (and
            ; IMPLEMENT
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
            ; IMPLEMENT
        )

        :effect (and
            ; IMPLEMENT
        )
    )

    ;Hero can clean a location if
    ;    - the hero is at location ?loc - location,
    ;    - the location is messy
    ;Effect will be that the location is no longer messy
    (:action clean

        :parameters (?loc - location)

        :precondition (and
            ; IMPLEMENT
        )

        :effect (and
            ; IMPLEMENT
        )
    )
)