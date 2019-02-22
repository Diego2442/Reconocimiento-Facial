


import obtener_dataset as tk
import reconocer_cara as rf



def main():
    steps = input("Bienvenidos al programa\n Opciones:\na. Presiona 1: para crear imagenes tuyas en el dataset y poder hacer training data(Solo se permite el ID 1, 2 no mas)\nb. Presione 2 para realizar la operacion\n> ")
    print('\n Use el ID  para probar la operacion')
    if(steps == '1'):
        tk.create_dataset()
        rf.run()
    elif(steps == '2'):
        suma = str(sum())
      

        image_recognized = tk.recognize()
        if image_recognized:
            print(f'El resultado es {suma}')
           
    else:
        print('Opcion no Valida')
        main()

def sum():
    numero1 = int(input('Introduce primer N.: '))
    numero2 = int(input('Introduce segundo N.: '))

    return numero1 + numero2

if __name__ == '__main__':
    main()