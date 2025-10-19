#!/usr/bin/env python3
"""
KSC 논문 DOCX 파일을 Markdown으로 변환하는 스크립트
"""

import os
import re
from pathlib import Path
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph


def extract_text_from_paragraph(paragraph):
    """단락에서 텍스트와 스타일 정보 추출"""
    text = paragraph.text.strip()
    if not text:
        return ""
    
    # 제목 스타일 감지
    if paragraph.style.name.startswith('Heading'):
        level = int(paragraph.style.name.replace('Heading ', ''))
        return f"{'#' * level} {text}\n"
    
    # 볼드체 감지 (대부분의 run이 볼드인 경우)
    bold_count = sum(1 for run in paragraph.runs if run.bold)
    if bold_count > len(paragraph.runs) / 2 and len(paragraph.runs) > 0:
        # 제목일 가능성이 있는 짧은 텍스트
        if len(text) < 100 and not text.endswith('.'):
            return f"## {text}\n"
    
    return f"{text}\n"


def extract_table_as_markdown(table):
    """테이블을 Markdown 형식으로 변환"""
    if not table.rows:
        return ""
    
    md_table = []
    
    # 테이블 헤더
    header_cells = [cell.text.strip() for cell in table.rows[0].cells]
    md_table.append("| " + " | ".join(header_cells) + " |")
    md_table.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
    
    # 테이블 본문
    for row in table.rows[1:]:
        cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
        md_table.append("| " + " | ".join(cells) + " |")
    
    return "\n".join(md_table) + "\n"


def convert_docx_to_markdown(docx_path, output_path):
    """DOCX 파일을 Markdown으로 변환"""
    print(f"변환 중: {docx_path.name}")
    
    try:
        doc = Document(docx_path)
        markdown_lines = []
        
        # 파일명에서 제목 추출
        title = docx_path.stem
        markdown_lines.append(f"# {title}\n")
        markdown_lines.append("---\n")
        
        # 문서 내용 처리
        for element in doc.element.body:
            if isinstance(element, CT_P):
                paragraph = Paragraph(element, doc)
                md_text = extract_text_from_paragraph(paragraph)
                if md_text:
                    markdown_lines.append(md_text)
            elif isinstance(element, CT_Tbl):
                table = Table(element, doc)
                md_table = extract_table_as_markdown(table)
                if md_table:
                    markdown_lines.append("\n" + md_table + "\n")
        
        # Markdown 파일 저장
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_lines))
        
        print(f"✓ 완료: {output_path.name}")
        return True
        
    except Exception as e:
        print(f"✗ 오류 발생 ({docx_path.name}): {e}")
        return False


def main():
    """메인 함수"""
    # 경로 설정
    base_dir = Path(__file__).parent
    input_dir = base_dir / "pdf-KSC"
    output_dir = base_dir / "md-KSC"
    
    # 출력 디렉토리 생성
    output_dir.mkdir(exist_ok=True)
    
    # DOCX 파일 목록
    docx_files = list(input_dir.glob("*.docx"))
    
    if not docx_files:
        print("변환할 DOCX 파일이 없습니다.")
        return
    
    print(f"\n총 {len(docx_files)}개의 DOCX 파일을 Markdown으로 변환합니다.\n")
    
    success_count = 0
    for docx_file in sorted(docx_files):
        output_file = output_dir / f"{docx_file.stem}.md"
        if convert_docx_to_markdown(docx_file, output_file):
            success_count += 1
        print()
    
    print(f"\n변환 완료: {success_count}/{len(docx_files)}개 성공")
    print(f"출력 디렉토리: {output_dir}")


if __name__ == "__main__":
    main()

