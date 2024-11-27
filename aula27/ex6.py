def cal_media(aluno):
    dic_media = {}
    for i in aluno:
        # print(i,aluno[i])
        dic_media[i]= sum(aluno[i])/4
    return dic_media

def al_mario_media(nota):
    media_M_sete = {}
    for i in nota:
        if nota[i]>=7:
            print(i, nota[i])
    

        


def main():
    alunos = {"Ana": [8.5, 7.0, 9.0, 6.5],
    "Carlos": [6.0, 5.5, 7.5, 8.0],
    "Beatriz": [9.0, 9.5, 8.0, 7.5],
    "João": [5.0, 6.5, 7.0, 6.0],
    "Mariana": [8.0, 7.5, 8.5, 9.0],
    "Pedro": [7.0, 6.5, 7.5, 7.0],
    "Luciana": [9.5, 8.0, 9.0, 9.5],
    "Felipe": [7.5, 6.0, 7.0, 6.5],
    "Fernanda": [8.5, 8.0, 7.5, 8.5],
    "Rafael": [6.5, 6.0, 6.5, 7.0]}

    cal_media(alunos)
    print('Alunos com media maior que a media 7:')
    al_mario_media(cal_media(alunos))

if __name__ == "__main__":
    main()