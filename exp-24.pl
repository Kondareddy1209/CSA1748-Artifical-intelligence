diet_suggestion(heart_disease, avoid(saturated_fats), eat(fruits), eat(vegetables), limit(sodium)).
diet_suggestion(diabetes, limit(sugar), eat(whole_grains), eat(lean_proteins), control(carbohydrates)).
diet_suggestion(hypertension, limit(sodium), eat(potassium-rich_foods), maintain(healthy_weight)).
suggest_diet_plan(Disease, DietPlan) :-
    disease_diet(Disease, DietPlan).
suggest_diet(Person, Disease, Suggestions) :-
    diet_suggestion(Disease, Suggestions),
    format('For ~w with ~w: ~w~n', [Person, Disease, Suggestions]).
disease_diet('Hypertension', [
    'Consume low-sodium foods.',
    'Increase intake of fruits and vegetables.',
    'Limit the consumption of processed and fatty foods.',
    'Reduce salt intake.',
    'Drink plenty of water.',
    'Consult a healthcare professional for a personalized plan.'
]).
disease_diet('Diabetes', [
    'Monitor your carbohydrate intake.',
    'Eat regular, balanced meals.',
    'Limit sugar and sugary beverages.',
    'Choose whole grains and high-fiber foods.',
    'Consult a dietitian for a personalized plan.'
]).
