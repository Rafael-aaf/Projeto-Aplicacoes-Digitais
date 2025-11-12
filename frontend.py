import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pokemon
import database

def search():
    pokemon_name = entry.get().lower().strip()
    if not pokemon_name:
        color = "white"
        root.configure(bg=color)
        nameLabel.config(text="Erro!", bg=color)
        idLabel.config(text="#0000", bg=color)
        weightLabel.config(text="Weight: \n", bg=color)
        heightLabel.config(text="Height: \n", bg=color)
        abilityLabel.config(text="Ability: \n", bg=color)
        typeLabel.config(text="Types: \n", bg=color)
        spriteLabel.config(image=tk_img, bg=color)
        spriteLabel.image = tk_img
        return
    
    pokemon_info = pokemon.get_pokemon_info(pokemon_name)
    
    if pokemon_info:
        data = pokemon.main(pokemon_info)

        database.inserir_pokemon(
            data["id"],
            data["name"],
            data["color"],
            data["weight"] / 10,
            data["height"] / 10,
            data["ability"]
        )

        url1 = data["sprite"]
        response = requests.get(url1)
        img_data = Image.open(BytesIO(response.content))
        img_data = img_data.resize((120, 120))
        img = ImageTk.PhotoImage(img_data)

        color = data["color"]
        idLabel.config(text=f'#{data["id"]}')
        nameLabel.config(text=data["name"])
        weightLabel.config(text=f'Weight: \n{data["weight"] / 10} kg')
        heightLabel.config(text=f'Height: \n{data["height"] / 10} m')
        abilityLabel.config(text=f'Ability: \n{data["ability"]}')

        types_text = "Types:\n"
        for t in data["types"]:
             types_text += f"- {t.capitalize()}\n"
             typeLabel.config(text=types_text)

        spriteLabel.config(image=img)
        spriteLabel.image = img

        if color != "black":
            root.configure(bg=color)
            idLabel.configure(bg=color)
            nameLabel.configure(bg=color)
            weightLabel.configure(bg=color)
            heightLabel.configure(bg=color)
            abilityLabel.configure(bg=color)
            typeLabel.configure(bg=color)
            spriteLabel.configure(bg=color)
        else:
            root.configure(bg="white")
            idLabel.configure(bg="white")
            nameLabel.configure(bg="white")
            weightLabel.configure(bg="white")
            heightLabel.configure(bg="white")
            abilityLabel.configure(bg="white")
            typeLabel.configure(bg="white")
            spriteLabel.configure(bg="white")
            

    else:
        nameLabel.config(text="Erro!")
        idLabel.config(text="#0000")
        weightLabel.config(text="Weight: \n")
        heightLabel.config(text="Height: \n")
        abilityLabel.config(text="Ability: \n")
        typeLabel.config(text="Types: \n")
        spriteLabel.config(image=tk_img)
        spriteLabel.image = tk_img

root = tk.Tk()
root.geometry("270x300")
root.title("POKEMON")
root.configure(bg="white")

#placeholder
transparent_img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
tk_img = ImageTk.PhotoImage(transparent_img)

#User Input
entry = tk.Entry(root, font = 8, borderwidth = 5)
entry.grid(row=0, column=0, columnspan=3, padx=5, pady=(10, 5))
entry.configure(bg="white")

#Button
button = tk.Button(root, text="click!", command=search)
button.grid(row=0, column=3, padx=5, pady=(10,5), sticky="E")

#Labels
idLabel = tk.Label(root, height=2, width=4, font=("Arial", 10, "bold"), text="#0000")
idLabel.grid(row=2, column=0, padx=5, pady=5, sticky="W")
idLabel.configure(bg="white")

nameLabel = tk.Label(root, height=2, width=10, font=("Arial", 10, "bold"), text="Name")
nameLabel.grid(row=2, column=1, pady=5)
nameLabel.configure(bg="white")

weightLabel = tk.Label(root, text="Weight: \n", font=("Arial", 10, "bold"))
weightLabel.grid(row=3, column=0, padx=5, pady=5, sticky="W")
weightLabel.configure(bg="white")

heightLabel = tk.Label(root, text="Height: ", font=("Arial", 10, "bold"))
heightLabel.grid(row=4, column=0, padx=5, pady=5, sticky="W")
heightLabel.configure(bg="white")

spriteLabel = tk.Label(root, image=tk_img)
spriteLabel.grid(row=3, rowspan=4, column=1, padx=5, pady=5, sticky="W")
spriteLabel.configure(bg="white")

abilityLabel = tk.Label(root, text="Ability: \n", font=("Arial", 10, "bold"))
abilityLabel.grid(row=7, column=0, columnspan=2,padx=5, pady=5, sticky="W")
abilityLabel.configure(bg="white")

typeLabel = tk.Label(root, text="Types: \n", font=("Arial", 10, "bold"))
typeLabel.grid(row=7, column=3, padx=5, pady=5, sticky="E")
typeLabel.configure(bg="white")

root.mainloop()