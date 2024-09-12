bird(canary).
bird(sparrow).
bird(ostrich).

can_fly(canary).
can_fly(sparrow).

% Query to check if a bird can fly
can_bird_fly(Bird) :-
    bird(Bird),
    can_fly(Bird).
