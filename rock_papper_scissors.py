while True :
  import random
  a=random.choice(["rock","pappers","scissors"])
  b=input("birini seçin(rock,pappers,scissors): ")
  if a=="rock" and b=="rock":
    print("berabere")
  if a=="rock" and b=="pappers":
    print("Siz qazandınız!")
  if a=="rock" and b=="scissors":
    print("Siz uduzdunuz")

  if a=="pappers" and b=="rock":
    print("siz uduzdunuz!")
  if a=="pappers" and b=="pappers":
    print("berabere")
  if a=="pappers" and b=="scissors":
    print("siz qazandınız!")

  if a=="scissors" and b=="rock":
    print('siz siz qazandınız!')
  if a=="scissors" and b=="pappers":
    print("siz uduzdunuz")
  if a=="scissors" and b=="scissors":
    print("berabere")
  