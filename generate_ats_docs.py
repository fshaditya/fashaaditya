import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

os.makedirs('downloads', exist_ok=True)

def create_ats_docx(filename, lang='id', is_full_cv=False):
    doc = docx.Document()
    
    # Page setup - 0.75 inch margins (Standard ATS Friendly)
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
    
    # Normal style font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(10)
    font.color.rgb = RGBColor(30, 41, 59)
    
    def add_heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text.upper())
        run.bold = True
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(15, 23, 42)
        
        # Add bottom border to heading (clean ATS single line divider)
        try:
            pBrd = parse_xml(
                '<w:pBrd xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                '<w:bottom w:val="single" w:sz="6" w:space="2" w:color="94A3B8"/>'
                '</w:pBrd>'
            )
            p._p.get_or_add_pPr().append(pBrd)
        except Exception:
            pass
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            run_b = p.add_run(bold_prefix)
            run_b.bold = True
        p.add_run(text)
        return p

    # --- Header ---
    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(2)
    run_name = p_name.add_run('FASHA ADITYA FEBRIANTO')
    run_name.bold = True
    run_name.font.size = Pt(18)
    run_name.font.color.rgb = RGBColor(15, 23, 42)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(4)
    run_sub = p_sub.add_run(
        'Teknik Industri (Industrial Engineering) • Institut Teknologi Nasional (ITENAS) Bandung'
        if lang == 'id'
        else 'Industrial Engineering Undergraduate • National Institute of Technology (ITENAS) Bandung'
    )
    run_sub.font.size = Pt(10)
    run_sub.font.color.rgb = RGBColor(71, 85, 105)

    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_after = Pt(10)
    run_contact = p_contact.add_run(
        'Bandung, Indonesia  |  fshaditya@gmail.com  |  linkedin.com/in/fashaaditya  |  github.com/fshaditya  |  fshaditya.github.io/fashaaditya'
    )
    run_contact.font.size = Pt(9.5)
    run_contact.font.color.rgb = RGBColor(71, 85, 105)

    # --- Summary ---
    add_heading('RINGKASAN PROFESIONAL' if lang == 'id' else 'PROFESSIONAL SUMMARY')
    p_sum = doc.add_paragraph()
    p_sum.paragraph_format.space_after = Pt(4)
    p_sum.paragraph_format.line_spacing = 1.15
    if lang == 'id':
        p_sum.add_run(
            'Mahasiswa Teknik Industri Institut Teknologi Nasional (ITENAS) Bandung angkatan 2025 dengan fokus keilmuan pada '
            'Perancangan Sistem Manufaktur, Analisis Ergonomi & Postur Kerja, Supply Chain & Manajemen Persediaan, serta Analisis Data Industri. '
            'Berpengalaman aktif dalam Google Developer Groups (GDG) On Campus dan kegiatan wirausaha regional ASEAN. Memiliki sertifikasi terverifikasi '
            'di bidang Data Analytics (Google Skillshop), Pemrograman Python (Dicoding), dan Artificial Intelligence. '
            'Terampil memadukan pendekatan analisis kuantitatif dengan pemecahan masalah operasional industri.'
        )
    else:
        p_sum.add_run(
            'Industrial Engineering undergraduate at Institut Teknologi Nasional (ITENAS) Bandung (Class of 2025) with specialized interests in '
            'Manufacturing Systems Optimization, Ergonomics, Supply Chain & Inventory Control, and Industrial Data Analytics. '
            'Certified in Google Data Analytics, Python programming, and Artificial Intelligence. Actively engaged in Google Developer Groups (GDG) On Campus '
            'and regional youth enterprise initiatives. Strong ability to integrate quantitative engineering methods with practical operational problem-solving.'
        )

    # --- Education ---
    add_heading('PENDIDIKAN' if lang == 'id' else 'EDUCATION')
    p_edu = doc.add_paragraph()
    p_edu.paragraph_format.space_before = Pt(2)
    p_edu.paragraph_format.space_after = Pt(2)
    r_inst = p_edu.add_run(
        'Institut Teknologi Nasional (ITENAS), Bandung'
        if lang == 'id'
        else 'National Institute of Technology (ITENAS), Bandung, Indonesia'
    )
    r_inst.bold = True
    p_edu.add_run('  |  2025 – Sekarang' if lang == 'id' else '  |  2025 – Present')

    p_deg = doc.add_paragraph()
    p_deg.paragraph_format.space_after = Pt(3)
    p_deg.add_run(
        'Sarjana Teknik (S1) - Teknik Industri'
        if lang == 'id'
        else 'Bachelor of Science (B.S.) in Industrial Engineering'
    ).italic = True

    if lang == 'id':
        add_bullet(
            'Relevansi Studi: ',
            'Perancangan Tata Letak Fasilitas Pabrik, Analisis Ergonomi & Pengukuran Kerja (RULA/REBA), Riset Operasional, Pengendalian Persediaan (EOQ/ROP), Pengendalian Mutu & K3 Industri.'
        )
        add_bullet(
            'Aktivitas: ',
            'Anggota Aktif Google Developer Groups (GDG) On Campus ITENAS, Panitia & Peserta Program BIG FAIR.'
        )
    else:
        add_bullet(
            'Relevant Coursework: ',
            'Facility Layout & Plant Design, Ergonomics & Biomechanical Posture Assessment (RULA/REBA), Operations Research, Inventory Control (EOQ/ROP), Statistical Quality Control.'
        )
        add_bullet(
            'Campus Activities: ',
            'Active Member at Google Developer Groups (GDG) On Campus ITENAS, Committee Member at BIG FAIR.'
        )

    # --- Skills ---
    add_heading('KEAHLIAN UTAMA & KOMPETENSI' if lang == 'id' else 'TECHNICAL & CORE SKILLS')
    if lang == 'id':
        add_bullet(
            'Kompetensi Teknik Industri: ',
            'Perancangan Tata Letak Fasilitas (Plant Layout/ARC), Analisis Ergonomi (RULA/REBA, Work Study), Pengendalian Persediaan (EOQ, ROP, Safety Stock), Simulasi Manufaktur, Toleransi Geometris (GD&T).'
        )
        add_bullet(
            'Digital & Analitik Data: ',
            'Google Data Analytics, Pemrograman Python (Pandas, NumPy, Matplotlib), Pemodelan Spreadsheet / Excel, Dasar Artificial Intelligence.'
        )
        add_bullet(
            'Perangkat Lunak Teknik: ',
            'SolidWorks CAD (3D Modeling & Kinematic Assembly), FDM 3D Printing (STL Slicing), Microsoft Visio, Draw.io.'
        )
        add_bullet(
            'Soft Skills & Bahasa: ',
            'Public Speaking, Komunikasi Multidisiplin, Manajemen Sumber Daya & Acara; Bahasa Indonesia (Native), Bahasa Inggris (Professional Working).'
        )
    else:
        add_bullet(
            'Industrial Engineering: ',
            'Plant Layout Optimization (ARC), Ergonomic Risk Assessment (RULA/REBA), Work Study, Inventory Modeling (EOQ, ROP, Safety Stock), GD&T Tolerancing, Quality Control.'
        )
        add_bullet(
            'Data & Programming: ',
            'Google Data Analytics, Python Programming (Pandas, NumPy, Matplotlib), Advanced Spreadsheet Modeling, Artificial Intelligence Fundamentals.'
        )
        add_bullet(
            'Engineering Software: ',
            'SolidWorks CAD (3D Modeling & Kinematic Assembly), FDM 3D Printing (STL Generation), Microsoft Visio, Draw.io.'
        )
        add_bullet(
            'Interpersonal & Languages: ',
            'Public Speaking, Cross-Functional Team Leadership, Event Coordination; Indonesian (Native), English (Professional Working Proficiency).'
        )

    # --- Projects ---
    add_heading('PROYEK TEKNIK INDUSTRI' if lang == 'id' else 'KEY ENGINEERING PROJECTS')

    # Project 1
    p_p1 = doc.add_paragraph()
    p_p1.paragraph_format.space_before = Pt(4)
    p_p1.paragraph_format.space_after = Pt(2)
    p_p1.paragraph_format.keep_with_next = True
    if lang == 'id':
        p_p1.add_run('1. Additive Manufacturing & 3D Printing Prototyping Komponen Ragum').bold = True
        p_p1.add_run(' | Lab SSML ITENAS')
        add_bullet(
            '',
            'Merancang komponen mekanikal individual ragum kerja bangku (bench vise), mengonversi geometri CAD ke format STL, menentukan parameter proses cetak FDM (infill density, layer height), serta memetakan alur kerja sistematis melalui diagram alir proses manufaktur.'
        )
    else:
        p_p1.add_run('1. Additive Manufacturing & 3D Printing Prototyping').bold = True
        p_p1.add_run(' | SSML Lab ITENAS')
        add_bullet(
            '',
            'Engineered individual mechanical CAD components for an industrial bench vise, optimized slicing process parameters (infill, layer height), and fabricated physical prototypes via FDM 3D printing with process flow diagramming.'
        )

    # Project 2
    p_p2 = doc.add_paragraph()
    p_p2.paragraph_format.space_before = Pt(3)
    p_p2.paragraph_format.space_after = Pt(2)
    p_p2.paragraph_format.keep_with_next = True
    if lang == 'id':
        p_p2.add_run('2. 3D Mechanical Assembly & ISO Standard Engineering Drawing Ragum SSML').bold = True
        p_p2.add_run(' | Lab SSML ITENAS')
        add_bullet(
            '',
            'Memodelkan rakitan mekanikal 3D (assembly) utuh 10+ part ragum pada SolidWorks dengan batasan suaian (mating). Menyusun lembar gambar kerja teknik 2D berstandar ISO lengkap dengan proyeksi ortogonal, penampang potong, etiket, Bill of Materials (BOM), dan toleransi geometris (GD&T).'
        )
    else:
        p_p2.add_run('2. 3D Mechanical Assembly & ISO Standard Engineering Drawing').bold = True
        p_p2.add_run(' | SSML Lab ITENAS')
        add_bullet(
            '',
            'Modeled 10+ part mechanical assembly of a precision bench vise mechanism using SolidWorks with kinematic mate constraints, drafting ISO-standard 2D fabrication blueprints, BOM, and GD&T specifications.'
        )

    # Project 3
    p_p3 = doc.add_paragraph()
    p_p3.paragraph_format.space_before = Pt(3)
    p_p3.paragraph_format.space_after = Pt(2)
    p_p3.paragraph_format.keep_with_next = True
    if lang == 'id':
        p_p3.add_run('3. Statistika Deskriptif & Pengendalian Variasi Mutu Bobot Produk Manufaktur').bold = True
        p_p3.add_run(' | Lab LKISI ITENAS')
        add_bullet(
            '',
            'Membangun skrip otomasi pengolahan data menggunakan Python (Pandas/NumPy) untuk evaluasi parameter tendensi sentral (Mean, Median, Modus) dan dispersi data (Variansi, Standar Deviasi, Kuantil, Boxplot) guna mendeteksi anomali variasi bobot produk manufaktur.'
        )
    else:
        p_p3.add_run('3. Descriptive Statistics & Manufacturing QC Variance Analysis').bold = True
        p_p3.add_run(' | LKISI Lab ITENAS')
        add_bullet(
            '',
            'Formulated an automated Python (Pandas/NumPy) pipeline to evaluate central tendency, product weight variance, and distribution parameters (skewness, kurtosis, boxplots) for manufacturing quality control inspection.'
        )

    # Project 4
    p_p4 = doc.add_paragraph()
    p_p4.paragraph_format.space_before = Pt(3)
    p_p4.paragraph_format.space_after = Pt(2)
    p_p4.paragraph_format.keep_with_next = True
    if lang == 'id':
        p_p4.add_run('4. Simulasi Distribusi Sampling & Validasi Empiris Central Limit Theorem').bold = True
        p_p4.add_run(' | Lab LKISI ITENAS')
        add_bullet(
            '',
            'Memodelkan simulasi komputasional distribusi sampling rata-rata bertingkat (N=2, 5, 10) berbasis Python. Menerapkan Aturan Sturges untuk penentuan kelas interval frekuensi serta membuktikan secara empiris konvergensi bentuk distribusi menuju kurva normal standar (CLT).'
        )
    else:
        p_p4.add_run('4. Sampling Distribution Simulation & Central Limit Theorem Validation').bold = True
        p_p4.add_run(' | LKISI Lab ITENAS')
        add_bullet(
            '',
            'Programmed multi-sample empirical simulations (N=2, 5, 10) using Sturges Rule binning and Matplotlib histograms to empirically demonstrate and validate Central Limit Theorem (CLT) convergence on operational data.'
        )

    # Project 5
    p_p5 = doc.add_paragraph()
    p_p5.paragraph_format.space_before = Pt(3)
    p_p5.paragraph_format.space_after = Pt(2)
    p_p5.paragraph_format.keep_with_next = True
    if lang == 'id':
        p_p5.add_run('5. Pengembangan Sistem Otomasi POS & Transaksi Loyalitas Pelanggan').bold = True
        p_p5.add_run(' | Lab LKISI ITENAS')
        add_bullet(
            '',
            'Memodelkan alur proses transaksi POS retail ke dalam diagram alir terstruktur menggunakan MS Visio. Mengimplementasikan program kalkulasi transaksi kasir berbasis Python dengan algoritma percabangan bersyarat, validasi format data, diskon keanggotaan loyalitas, dan pembuatan kode unik transaksi.'
        )
    else:
        p_p5.add_run('5. Automated Retail POS & Customer Loyalty Transaction System').bold = True
        p_p5.add_run(' | LKISI Lab ITENAS')
        add_bullet(
            '',
            'Designed system flowcharts in MS Visio and implemented a Python CLI checkout engine featuring multi-condition branching, automated unique order token generation, and customer loyalty cashback calculations.'
        )

    # --- Certifications ---
    add_heading('SERTIFIKASI & KREDENSIAL' if lang == 'id' else 'CERTIFICATIONS & CREDENTIALS')
    certs = [
        ('Google Data Analytics Course', 'Google Skillshop', '2025', 'CERT-GGL-DATA-2025'),
        ('AI for Everyone', 'AI Competency Certification', '2025', 'CERT-AI-EVERYONE-2025'),
        ('Memulai Pemrograman dengan Python' if lang == 'id' else 'Programming with Python', 'Dicoding Academy', '2025', 'CERT-DCD-PYTHON-2025'),
        ('BIG FAIR CAYE ASEAN 2026 (Singapore & Malaysia)', 'CAYE ASEAN • BIG FAIR', '2026', 'CERT-CAYE-ASEAN-2026'),
        ('Human Capital Excellence & Public Speaking', 'BIG FAIR ITENAS', '2025', 'CERT-HC-BIGFAIR-2025'),
        ('Introduction to Financial Literacy', 'Dicoding Academy', '2025', 'CERT-DCD-FIN-2025'),
        ('POLBAN Entrepreneur Day 2025', 'Politeknik Negeri Bandung', '2025', 'CERT-POLBAN-ENT-2025'),
        ('Active Membership Certification', 'Google Developer Groups (GDG) On Campus', '2025', 'CERT-GDG-CAMPUS-2025'),
    ]
    for c_title, c_issuer, c_year, c_id in certs:
        add_bullet(f'{c_title} – {c_issuer} ({c_year})', f' | Doc ID: {c_id}')

    # --- Leadership / Organizations ---
    add_heading('PENGALAMAN ORGANISASI' if lang == 'id' else 'ORGANIZATIONAL & LEADERSHIP EXPERIENCE')
    if lang == 'id':
        p_o1 = doc.add_paragraph()
        p_o1.paragraph_format.space_before = Pt(3)
        p_o1.paragraph_format.space_after = Pt(2)
        p_o1.paragraph_format.keep_with_next = True
        p_o1.add_run('Google Developer Groups (GDG) On Campus ITENAS').bold = True
        p_o1.add_run(' | Active Member (2025 – Sekarang)')
        add_bullet(
            '',
            'Terlibat aktif dalam lokakarya teknologi, pengenalan ekosistem komputasi Google, dan kolaborasi pengembangan solusi digital bersama komunitas kampus.'
        )

        p_o2 = doc.add_paragraph()
        p_o2.paragraph_format.space_before = Pt(3)
        p_o2.paragraph_format.space_after = Pt(2)
        p_o2.paragraph_format.keep_with_next = True
        p_o2.add_run('Kepanitiaan BIG FAIR ITENAS').bold = True
        p_o2.add_run(' | Divisi Human Capital & Content Creator (2025 – 2026)')
        add_bullet(
            '',
            'Mengelola koordinasi sumber daya manusia relawan, memfasilitasi sesi komunikasi publik, dan memproduksi konten informasi program berskala regional.'
        )

        p_o3 = doc.add_paragraph()
        p_o3.paragraph_format.space_before = Pt(3)
        p_o3.paragraph_format.space_after = Pt(2)
        p_o3.paragraph_format.keep_with_next = True
        p_o3.add_run('Delegasi BIG FAIR CAYE ASEAN 2026 (Singapore & Malaysia)').bold = True
        p_o3.add_run(' | Delegasi Internasional (2026)')
        add_bullet(
            '',
            'Berpartisipasi dalam agenda pertukaran wawasan kewirausahaan dan industri pemuda lintas negara ASEAN, memperluas jejaring profesional di Singapura dan Malaysia.'
        )
    else:
        p_o1 = doc.add_paragraph()
        p_o1.paragraph_format.space_before = Pt(3)
        p_o1.paragraph_format.space_after = Pt(2)
        p_o1.paragraph_format.keep_with_next = True
        p_o1.add_run('Google Developer Groups (GDG) On Campus ITENAS').bold = True
        p_o1.add_run(' | Active Member (2025 – Present)')
        add_bullet(
            '',
            'Actively participated in technology enablement sessions, Google developer ecosystems exploration, and student digital innovation initiatives.'
        )

        p_o2 = doc.add_paragraph()
        p_o2.paragraph_format.space_before = Pt(3)
        p_o2.paragraph_format.space_after = Pt(2)
        p_o2.paragraph_format.keep_with_next = True
        p_o2.add_run('BIG FAIR ITENAS Committee').bold = True
        p_o2.add_run(' | Human Capital & Content Creator (2025 – 2026)')
        add_bullet(
            '',
            'Coordinated volunteer human capital operations, delivered public speaking presentations, and developed digital outreach content.'
        )

        p_o3 = doc.add_paragraph()
        p_o3.paragraph_format.space_before = Pt(3)
        p_o3.paragraph_format.space_after = Pt(2)
        p_o3.paragraph_format.keep_with_next = True
        p_o3.add_run('CAYE ASEAN Delegation (Singapore & Malaysia)').bold = True
        p_o3.add_run(' | International Delegate (2026)')
        add_bullet(
            '',
            'Represented youth enterprise delegate in cross-border innovation and industrial networking summits across Singapore and Malaysia.'
        )

    doc.save(filename)
    print(f'Generated: {filename} ({os.path.getsize(filename)} bytes)')

if __name__ == '__main__':
    create_ats_docx('downloads/Resume_Fasha_Aditya_Febrianto_ATS.docx', lang='id')
    create_ats_docx('downloads/Resume_Fasha_Aditya_Febrianto_EN_ATS.docx', lang='en')
    create_ats_docx('downloads/CV_Fasha_Aditya_Febrianto_ATS.docx', lang='id', is_full_cv=True)
