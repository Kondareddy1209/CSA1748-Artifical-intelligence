symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, nausea).

% Facts representing diseases and their associated symptoms
disease(flu, fever).
disease(flu, cough).
disease(stress, headache).
disease(food_poisoning, nausea).

% Rule to determine if a person has a specific symptom
has_symptom(Person, Symptom) :-
    symptom(Person, Symptom).

% Rule to determine if a person has a specific disease
has_disease(Person, Disease) :-
    has_symptom(Person, Symptom),
    disease(Disease, Symptom).

% Backward chaining rule
backward_chaining(Person, Disease) :-
    has_disease(Person, Disease),
    write(Person), write(' is diagnosed with '), write(Disease), nl.
