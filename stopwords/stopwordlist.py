def get_stop_words() -> set:
    """ return set(stopword list)

    불용어 사전 불러오기(stopwordlist.txt)
    파일이 없으면 기본 불용어 사전을 사용

    Returns:
        set(stopwordlist.txt)set 형식의 불용어 사전

    """
    try:
        with open('stopwordlist.txt', 'r') as f:
            txt_lines = f.read().splitlines()

        comments = [line for line in txt_lines if '#' in line]
        print(comments)     # 불용어 사전 정보 출력

        stop_word_list = [line for line in txt_lines if '#' not in line]

    except FileNotFoundError:
        stop_word_list = ['\n', '을', '를', '은', '가', '는', '이', '도', '수', '며', '고', 'nan', '우리', '저희', '단지', '기여', '오후', '매우', '여러분', '얘기', '인사', '아마', '추정', '언급', '지금', '질문', '중요', '결정', '다음', '제가', '정도', '고려', '사실', '이후', '현재', '문제', '말씀', '사람', '경제', '생각', '말씀']      # 기본 불용어
        
    return set(stop_word_list)


def main():
    stopword_list = get_stop_words()
    print('::불용어 목록::')
    print(stopword_list)


if __name__ == '__main__':
    main()
