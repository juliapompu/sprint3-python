import re
import time
import json
import os
import uuid

class RedeSocialFutebolFeminino:
    def __init__(self):
        self.usuario_logado = None
        self.videos = []
        self.curtidas = []  
        self.arquivo_usuarios = 'usuarios.json'
        self.arquivo_videos = 'videos.json'
        self.arquivo_curtidas = 'curtidas.json'  
        
        self.usuarios = self.carregar_usuarios()
        self.videos = self.carregar_videos()
        self.curtidas = self.carregar_curtidas()

        self.adicionar_usuarios_exemplo()
        self.adicionar_videos_exemplo()

    def carregar_usuarios(self):
        if os.path.exists(self.arquivo_usuarios):
            try:
                with open(self.arquivo_usuarios, 'r', encoding='utf-8') as arquivo:
                    return json.load(arquivo)
            except:
                return []
        return []
    
    def carregar_videos(self):
        if os.path.exists(self.arquivo_videos):
            try:
                with open(self.arquivo_videos, 'r', encoding='utf-8') as arquivo:
                    return json.load(arquivo)
            except:
                return []
        return []
    
    def carregar_curtidas(self):
        if os.path.exists(self.arquivo_curtidas):
            try:
                with open(self.arquivo_curtidas, 'r', encoding='utf-8') as arquivo:
                    return json.load(arquivo)
            except:
                return []
        return []
    
    def salvar_usuarios(self):
        try:
            with open(self.arquivo_usuarios, 'w', encoding='utf-8') as arquivo:
                json.dump(self.usuarios, arquivo, ensure_ascii=False, indent=2)
        except:
            print("Erro ao salvar usuários!")
    
    def salvar_videos(self):
        try:
            with open(self.arquivo_videos, 'w', encoding='utf-8') as arquivo:
                json.dump(self.videos, arquivo, ensure_ascii=False, indent=2)
        except:
            print("Erro ao salvar vídeos!")
    
    def salvar_curtidas(self):
        try:
            with open(self.arquivo_curtidas, 'w', encoding='utf-8') as arquivo:
                json.dump(self.curtidas, arquivo, ensure_ascii=False, indent=2)
        except:
            print("Erro ao salvar curtidas!")
    
    def adicionar_usuarios_exemplo(self):
        usuarios_exemplo = [
            {
                'email': 'jogadora10@gmail.com',
                'senha': 'senha123',
                'username': 'jogadora10',
                'nome_real': 'Maria Silva',
                'tipo': 'jogadora',
                'biografia': 'Jogadora profissional de futebol ⚽'
            },
            {
                'email': 'carol_goleira@gmail.com',
                'senha': 'senha123',
                'username': 'carol_goleira',
                'nome_real': 'Carolina Santos',
                'tipo': 'jogadora',
                'biografia': 'Goleira apaixonada pelo esporte 🧤'
            },
            {
                'email': 'bia_torcedora@gmail.com',
                'senha': 'senha123',
                'username': 'bia_torcedora',
                'nome_real': 'Beatriz Oliveira',
                'tipo': 'torcedora',
                'biografia': 'Torcedora fanática do futebol feminino! 💜'
            }
        ]
        
        for usuario_exemplo in usuarios_exemplo:
            if not any(u['email'] == usuario_exemplo['email'] for u in self.usuarios):
                self.usuarios.append(usuario_exemplo)
        
        self.salvar_usuarios()
    
    def adicionar_videos_exemplo(self):
        videos_exemplo = [
            {
                'id': str(uuid.uuid4()),
                'titulo': 'Gol incrível no último minuto! ⚽️',
                'descricao': 'Gol de falta decisivo no clássico contra o maior rival. Que emoção!',
                'autor': 'jogadora10',
                'link': "https://example.com/video1",
                'visualizacoes': 12500,
                'likes': 980,
                'curtidas': [],
                'comentarios': [
                    {"usuario_id": '', "comentario": "Que golaço! Parabéns! 🎉"},
                    {"usuario_id": '', "comentario": "Incrível! Você merece todo esse sucesso! 👏"},
                    {"usuario_id": '', "comentario": "Inspiração para todas nós! Continue brilhando! ✨"},
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'titulo': 'Melhores defesas da temporada 🧤',
                'descricao': 'Compilação das defesas que garantiram nossa classificação!',
                'autor': 'carol_goleira',
                'link': "https://example.com/video2",
                'visualizacoes': 8900,
                'likes': 750,
                'curtidas': [],
                'comentarios': [
                    {"usuario_id": '', "comentario": "Você é uma parede! Incrível! 🙌"},
                ]
            },
            {
                'id': str(uuid.uuid4()),
                'titulo': 'Momento emocionante do campeonato 🏆',
                'descricao': 'Editando os lances mais incríveis da temporada! #PaixãoPeloFutebol',
                'autor': 'bia_torcedora',
                'link': "https://example.com/video3",
                'visualizacoes': 15600,
                'likes': 1200,
                'curtidas': [],
                'comentarios': [
                    {"usuario_id": '', "comentario": "Amo esse vídeo! Futebol feminino é tudo! 💜"},
                    {"usuario_id": '', "comentario": "Muito orgulho de fazer parte dessa comunidade! Vamos juntas! 💪"},
                ]
            }
        ]
        if not self.videos:
            self.videos = videos_exemplo
            self.salvar_videos()

    def postar_video(self):
        print("\n" + "="*40)
        print("🎥 POSTAR NOVO VÍDEO")
        print("="*40)
        titulo = input("Título do vídeo: ").strip()
        descricao = input("Descrição: ").strip()
        link = input("Link do vídeo: ").strip()
        if not (titulo and descricao and link):
            print("❌ Todos os campos são obrigatórios!")
            return
        novo_video = {
            'id': str(uuid.uuid4()),
            'titulo': titulo,
            'descricao': descricao,
            'autor': self.usuario_logado['username'],
            'link': link,
            'visualizacoes': 0,
            'likes': 0,
            'curtidas': [],
            'comentarios': []
        }
        self.videos.append(novo_video)
        self.salvar_videos()
        print("✅ Vídeo postado com sucesso!")

    def validar_email(self, email):
        formato_valido = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        return re.match(formato_valido, email) is not None

    def fazer_login(self):
        print("\n" + "="*40)
        print("🎯 ENTRAR NA CONTA")
        print("="*40)
        
        email = input("📧 Email: ").strip()
        senha = input("🔒 Senha: ")
        
        for usuario in self.usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                self.usuario_logado = usuario
                print(f"\n✅ Bem-vinda de volta, {usuario['nome_real']}!")
                time.sleep(1)
                return True
        
        print("\n❌ Email ou senha incorretos!")
        time.sleep(1)
        return False

    def fazer_cadastro(self):
        print("\n" + "="*40)
        print("🌟 CRIAR NOVA CONTA")
        print("="*40)
        
        while True:
            email = input("📧 Email (@gmail.com): ").strip()
            if not self.validar_email(email):
                print("❌ Email inválido! Use um email @gmail.com")
                continue
            
            if any(u['email'] == email for u in self.usuarios):
                print("❌ Este email já está cadastrado!")
                continue
            
            break
        
        while True:
            senha = input("🔒 Senha (mínimo 6 letras/números): ")
            if len(senha) >= 6:
                break
            print("❌ Senha muito curta! Precisa ter pelo menos 6 caracteres.")
        
        while True:
            username = input("👤 Nome de usuário: ").strip()
            if username:
                if any(u['username'] == username for u in self.usuarios):
                    print("❌ Este nome de usuário já existe!")
                else:
                    break
            else:
                print("❌ Nome de usuário não pode ficar vazio!")
        
        while True:
            nome_real = input("👋 Seu nome real: ").strip()
            if nome_real:
                break
            print("❌ Nome real não pode ficar vazio!")
        
        while True:
            tipo = input("⚽ Você é jogadora ou torcedora? ").strip().lower()
            if tipo in ['jogadora', 'torcedora']:
                break
            print("❌ Digite 'jogadora' ou 'torcedora'!")
        
        biografia = input("📝 Conte um pouco sobre você: ").strip()
        if not biografia:
            biografia = "Novo membro da comunidade do futebol feminino! 💪"
        
        novo_usuario = {
            'email': email,
            'id': str(uuid.uuid4()),
            'senha': senha,
            'username': username,
            'nome_real': nome_real,
            'tipo': tipo,
            'biografia': biografia
        }
        
        self.usuarios.append(novo_usuario)
        self.usuario_logado = novo_usuario
        self.salvar_usuarios()
        
        print(f"\n🎉 Conta criada com sucesso! Bem-vinda, {nome_real}!")
        time.sleep(1)

    def tela_inicial(self):
        while True:
            print("\n" + "="*40)
            print("⚽ REDE SOCIAL DO FUTEBOL FEMININO")
            print("="*40)
            print("1. Entrar na minha conta")
            print("2. Criar nova conta")
            print("3. Sair do programa")
            print("="*40)
            
            try:
                escolha = int(input("👉 Escolha uma opção: "))
                
                if escolha == 1:
                    if self.fazer_login():
                        self.menu_principal()
                elif escolha == 2:
                    self.fazer_cadastro()
                    self.menu_principal()
                elif escolha == 3:
                    print("👋 Até logo! Volte sempre!")
                    break
                else:
                    print("❌ Opção inválida! Escolha 1, 2 ou 3.")
            
            except ValueError:
                print("❌ Por favor, digite apenas números!")

    def menu_principal(self):
        while self.usuario_logado:
            print("\n" + "="*40)
            print("🏠 MENU PRINCIPAL")
            print("="*40)
            print(f"👋 Olá, {self.usuario_logado['nome_real']}!")
            print("="*40)
            print("1. 👤 Meu perfil")
            print("2. 📺 Ver vídeos")
            print("3. 🎥 Postar vídeo")
            print("4. ✏️ Editar perfil")
            print("5. 🚪 Sair da conta")
            print("="*40)
            
            try:
                escolha = int(input("👉 Escolha uma opção: "))
                
                if escolha == 1:
                    self.ver_meu_perfil()
                elif escolha == 2:
                    self.ver_videos()
                elif escolha == 3:
                    self.postar_video()
                elif escolha == 4:
                    self.editar_perfil()
                elif escolha == 5:
                    print("👋 Saindo da sua conta...")
                    self.usuario_logado = None
                    break
                else:
                    print("❌ Opção inválida!")
            
            except ValueError:
                print("❌ Por favor, digite apenas números!")

    def ver_meu_perfil(self):
        print("\n" + "="*50)
        print("👤 MEU PERFIL")
        print("="*50)
        print(f"👤 Nome de usuário: @{self.usuario_logado['username']}")
        print(f"👋 Nome real: {self.usuario_logado['nome_real']}")
        print(f"📧 Email: {self.usuario_logado['email']}")
        print(f"⚽ Tipo: {self.usuario_logado['tipo'].capitalize()}")
        print(f"📝 Biografia: {self.usuario_logado['biografia']}")
        print("="*50)
        
        input("\n⏎ Pressione Enter para voltar...")

    def editar_perfil(self):
        print("\n" + "="*40)
        print("✏️ EDITAR PERFIL")
        print("="*40)
        
        indice_usuario = None
        for i, usuario in enumerate(self.usuarios):
            if usuario['email'] == self.usuario_logado['email']:
                indice_usuario = i
                break
        
        if indice_usuario is None:
            print("❌ Erro: Não encontrei seu perfil!")
            return
        
        while True:
            print("\n📋 O que você quer editar?")
            print("1. 👤 Nome de usuário")
            print("2. 👋 Nome real")
            print("3. 📝 Biografia")
            print("4. 🔒 Senha")
            print("5. ↩️ Voltar ao menu")
            
            try:
                escolha_editar = int(input("\n👉 Escolha uma opção: "))
                
                if escolha_editar == 1:
                    self.editar_username(indice_usuario)
                elif escolha_editar == 2:
                    self.editar_nome_real(indice_usuario)
                elif escolha_editar == 3:
                    self.editar_biografia(indice_usuario)
                elif escolha_editar == 4:
                    self.editar_senha(indice_usuario)
                elif escolha_editar == 5:
                    break
                else:
                    print("❌ Opção inválida!")
            
            except ValueError:
                print("❌ Por favor, digite apenas números!")

    def editar_username(self, indice_usuario):
        while True:
            novo_username = input("👤 Novo nome de usuário: ").strip()
            if not novo_username:
                print("❌ Nome de usuário não pode ficar vazio!")
                continue
            
            if any(u['username'] == novo_username and u['email'] != self.usuario_logado['email'] for u in self.usuarios):
                print("❌ Este nome já está sendo usado!")
                continue
            
            self.usuarios[indice_usuario]['username'] = novo_username
            self.usuario_logado['username'] = novo_username
            self.salvar_usuarios()
            print("✅ Nome de usuário atualizado!")
            break

    def editar_nome_real(self, indice_usuario):
        while True:
            novo_nome = input("👋 Novo nome real: ").strip()
            if not novo_nome:
                print("❌ Nome real não pode ficar vazio!")
                continue
            
            self.usuarios[indice_usuario]['nome_real'] = novo_nome
            self.usuario_logado['nome_real'] = novo_nome
            self.salvar_usuarios()
            print("✅ Nome real atualizado!")
            break

    def editar_biografia(self, indice_usuario):
        nova_biografia = input("📝 Nova biografia: ").strip()
        if not nova_biografia:
            nova_biografia = "Amante do futebol feminino! 💪"
        
        self.usuarios[indice_usuario]['biografia'] = nova_biografia
        self.usuario_logado['biografia'] = nova_biografia
        self.salvar_usuarios()
        print("✅ Biografia atualizada!")

    def editar_senha(self, indice_usuario):
        while True:
            nova_senha = input("🔒 Nova senha (mínimo 6 caracteres): ")
            if len(nova_senha) >= 6:
                self.usuarios[indice_usuario]['senha'] = nova_senha
                self.usuario_logado['senha'] = nova_senha
                self.salvar_usuarios()
                print("✅ Senha atualizada!")
                break
            else:
                print("❌ Senha muito curta! Mínimo 6 caracteres.")

    def ver_videos(self):
        if not self.videos:
            print("\n📺 Nenhum vídeo ainda. Seja a primeira a postar!")
            input("\n⏎ Pressione Enter para voltar...")
            return
        
        indice_atual = 0
        
        while True:
            video = self.videos[indice_atual]
            
            print("\n" + "="*60)
            print("📺 FEED DE VÍDEOS")
            print("="*60)
            print(f"🎬 Vídeo {indice_atual + 1} de {len(self.videos)}")
            print("="*60)
            print(f"📌 Título: {video['titulo']}")
            print(f"📝 Descrição: {video['descricao']}")
            print(f"👤 Por: @{video['autor']}")
            print(f"🔗 Link: {video['link']}")
            print(f"👁️  {video['visualizacoes']} visualizações")
            print(f"❤️  {video['likes']} curtidas")
            print("="*60)
            
            print("\n🎮 Navegação:")
            if indice_atual > 0:
                print("1. ⬅️  Vídeo anterior")
            if indice_atual < len(self.videos) - 1:
                print("2. ➡️  Próximo vídeo")
            print("3. 👤 Ver perfil de @" + video['autor'])
            print("4. ❤️ Curtir este vídeo")
            print("5. 💬 Comentar neste vídeo")
            print("6. 👀 Ver comentários")
            print("7. ↩️  Voltar ao menu")
            
            try:
                escolha = int(input("\n👉 Escolha uma opção: "))
                
                if escolha == 1 and indice_atual > 0:
                    indice_atual -= 1
                elif escolha == 2 and indice_atual < len(self.videos) - 1:
                    indice_atual += 1
                elif escolha == 3:
                    # Buscar o autor pelo username
                    autor = next((u for u in self.usuarios if u['username'] == video['autor']), None)
                    if autor:
                        self.ver_perfil_autor(autor['id'])
                    else:
                        print("❌ Autor não encontrado!")
                elif escolha == 4:
                    self.curtir_video(indice_atual)
                elif escolha == 5:
                    self.comentar_video(indice_atual)
                elif escolha == 6:
                    self.ver_comentarios_video(indice_atual)
                elif escolha == 7:
                    break
                else:
                    print("❌ Opção inválida!")

            except ValueError:
                print("❌ Por favor, digite apenas números!")

    def curtir_video(self, indice_video):
        video = self.videos[indice_video]
        if 'curtidas' not in video:
            video['curtidas'] = []
        
        user_id = self.usuario_logado.get('id')
        video_id = video.get('id')
        if not video_id:
            # Gerar um ID único para o vídeo se não existir
            video_id = str(uuid.uuid4())
            video['id'] = video_id
            self.salvar_videos()
        
        # Verifica se o usuário já curtiu
        if user_id not in video['curtidas']:
            video['curtidas'].append(user_id)
            video['likes'] += 1
            self.salvar_videos()
            
            # Registrar a curtida
            registro = {
                "tipo": "curtida",
                "usuario_id": user_id,
                "video_id": video_id,
                "data": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            self.curtidas.append(registro)
            self.salvar_curtidas()
            
            print("❤️ Você curtiu este vídeo!")
        else:
            print("❌ Você já curtiu este vídeo.")

    def comentar_video(self, indice_video):
        comentario = input("💬 Escreva seu comentário: ").strip()
        if comentario:
            if 'comentarios' not in self.videos[indice_video]:
                self.videos[indice_video]['comentarios'] = []
            
            user_id = self.usuario_logado.get('id')
            video = self.videos[indice_video]
            video_id = video.get('id')
            if not video_id:
                video_id = str(uuid.uuid4())
                video['id'] = video_id
                self.salvar_videos()
            
            novo_comentario = {
                'usuario_id': user_id,
                'comentario': comentario
            }
            self.videos[indice_video]['comentarios'].append(novo_comentario)
            self.salvar_videos()

            # Registrar o comentário
            registro = {
                "tipo": "comentario",
                "usuario_id": user_id,
                "video_id": video_id,
                "comentario": comentario,
                "data": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            self.curtidas.append(registro)
            self.salvar_curtidas()

            print("✅ Comentário adicionado!")
        else:
            print("❌ Comentário vazio não foi adicionado.")

    def ver_comentarios_video(self, indice_video):
        comentarios = self.videos[indice_video].get('comentarios', [])
        if not comentarios:
            print("\n💬 Nenhum comentário ainda. Seja a primeira a comentar!")
        else:
            print("\n" + "="*40)
            print("💬 COMENTÁRIOS")
            print("="*40)
            for c in comentarios:
                usuario = self.buscar_usuario_por_id(c.get('usuario_id'))
                username = usuario['username'] if usuario else 'desconhecido'
                print(f"👤 @{username}: {c['comentario']}")
                print("-"*40)
        
        input("\n⏎ Pressione Enter para voltar...")

    # buscar usuário por id
    def buscar_usuario_por_id(self, user_id):
        for usuario in self.usuarios:
            if usuario.get('id') == user_id:
                return usuario
        return None

    def buscar_video_por_id(self, video_id):
        for video in self.videos:
            if video.get('id') == video_id:
                return video
        return None

    # ver perfil do autor
    def ver_perfil_autor(self, id_autor):
        autor = self.buscar_usuario_por_id(id_autor)
        if autor:
            print("\n" + "="*50)
            print("👤 PERFIL DO AUTOR")
            print("="*50)
            print(f"👤 Nome de usuário: @{autor['username']}")
            print(f"👋 Nome real: {autor['nome_real']}")
            print(f"⚽ Tipo: {autor['tipo'].capitalize()}")
            print(f"📝 Biografia: {autor['biografia']}")
            print("="*50)
        else:
            print("❌ Autor não encontrado!")
        input("\n⏎ Pressione Enter para voltar...")


if __name__ == "__main__":
    print("⚽ Iniciando Rede Social do Futebol Feminino...")
    time.sleep(1)
    rede_social = RedeSocialFutebolFeminino()
    rede_social.tela_inicial()