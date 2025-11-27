def draw_rectangle(w, h):
    for i in range(h):

        ligne = "|"

        if i == 0 or i == h-1:
            for i in range(w-2):
                ligne += "-"           
        else:
            for i in range(w-2):
                ligne += " "

        ligne += "|"

        print(ligne)

draw_rectangle(10, 3)

# bruh bruh commit