# 메인 스크립트

from scripts.get_trending_keywords import get_nate_pann_trending_keywords
from scripts.generate_blog_content import generate_blog_content
from scripts.post_to_tistory import post_to_tistory

def main():
    trending_keywords = get_nate_pann_trending_keywords()
    print(f"Trending Keywords: {trending_keywords}")

    if trending_keywords:
            popular_keyword = trending_keywords[0]  # 가장 인기 있는 키워드 선택
            content = generate_blog_content(popular_keyword)
            print(f"제목 :: {content}\n")

if __name__ == "__main__":
    main()