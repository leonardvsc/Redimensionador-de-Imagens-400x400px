from PIL import Image
import os

def redimensionar_imagens(caminho_pasta):
    for arquivo in os.listdir(caminho_pasta):
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        try:
            imagem = Image.open(caminho_arquivo)
            imagem = imagem.convert("RGB")
            
            # Redimensionar a imagem para caber dentro do quadrado de 400x400 mantendo a proporção
            imagem.thumbnail((400, 400))
            
            # Criar uma nova imagem em branco de 400x400 pixels com a margem
            imagem_quadrada = Image.new("RGB", (400, 400), (255, 255, 255))
            
            # Calcular a margem de 5 pixels em cada lado para a imagem de maior proporção
            margem_horizontal = (400 - imagem.width) // 2
            margem_vertical = (400 - imagem.height) // 2
            
            # Ampliar a imagem se for menor que 390 pixels em qualquer dimensão
            if imagem.width < 390 or imagem.height < 390:
                proporcao = min(390 / imagem.width, 390 / imagem.height)
                nova_largura = int(imagem.width * proporcao)
                nova_altura = int(imagem.height * proporcao)
                imagem = imagem.resize((nova_largura, nova_altura))
                margem_horizontal = (400 - nova_largura) // 2
                margem_vertical = (400 - nova_altura) // 2
            
            # Colocar a imagem redimensionada no centro do quadrado com a margem
            imagem_quadrada.paste(imagem, (margem_horizontal, margem_vertical))
            
            # Salvar a imagem com o mesmo nome do arquivo original
            imagem_quadrada.save(caminho_arquivo)
            
        except Exception as e:
            print(f"Erro ao processar a imagem {caminho_arquivo}: {str(e)}")

caminho_pasta = r"C:\Users\Grafica\Desktop\Redimensionamento"
redimensionar_imagens(caminho_pasta)
