release: python manage.py migrate --noinput   #"release: python manage.py migrate" aqui fazendo o migrate das nossas aplicações. E esse "--noinput" é quando o programa pergunta se a gente tem certeza, que quer rodar as migrações, esse código agiliza essa parte. Esse comando vai aplicar nossas migrações la no servidor. Pois até agora nosso programa roda apenas no nosso computador
web: gunicorn devpro.wsgi --log-file -    #"--log-file - "aqui é para colocar os logs do servidor em um arquivo

