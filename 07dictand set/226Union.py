farm_animal={"sheep","heen","cow","horse","goat"}
wild_animla={"lion","elephant","tiger","goat","panther","horse"}

all_animal=farm_animal.union(wild_animla)
print(all_animal)

all_animal3=farm_animal | wild_animla
print(all_animal3)