from utils import unpickle_prefect_res

p1 = "prefect_results/DOG_FLOW/19-01_23-39-42/cat-d2b5af9f-0ffc-440e-947c-f805bdae4a72.prefect_result"
p2 = "prefect_results/DOG_FLOW/19-01_23-39-42/puppy-710568ff-cda5-43a6-a1e1-d9c7386b1d63.prefect_result"
p3 = "prefect_results/DOG_FLOW/19-01_23-39-42/SQL-stuff-372e2ac4-9480-4274-bfff-83492ff3b2cc.prefect_result"

for file in [p1,p2,p3]:
    print(unpickle_prefect_res(file))