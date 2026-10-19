from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Данные о торрентах
torrents_data = [
    {
        'id': '1',
        'name': 'Дюна: Часть вторая (2024) BDRip 4K | HDR | DUB',
        'size': '45.2 GB',
        'seeds': 1542,
        'leechers': 328,
        'downloads': 24500,
        'upload_date': '2024-06-15',
        'category': 'Фильмы',
        'tags': ['movies', '4k', 'hdr', 'bdrip', 'rus', 'scifi', 'action', 'drama', '12+'],
        'magnet_link': 'magnet:?xt=urn:btih:example1',
        'quality': '4K HDR',
        'language': 'Русский (дубляж)',
    },
    {
        'id': '2',
        'name': 'The Last of Us / Остаться в живых (2024) S02 WEB-DL 1080p | LostFilm',
        'size': '32.8 GB',
        'seeds': 2103,
        'leechers': 456,
        'downloads': 31200,
        'upload_date': '2024-05-20',
        'category': 'Сериалы',
        'tags': ['series', '1080p', 'webdl', 'rus', 'drama', 'action', 'thriller', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example2',
        'quality': '1080p',
        'language': 'Русский (LostFilm)',
    },
    {
        'id': '3',
        'name': 'Cyberpunk 2077: Phantom Liberty [v2.1] (2024) PC | RePack',
        'size': '58.3 GB',
        'seeds': 876,
        'leechers': 234,
        'downloads': 15600,
        'upload_date': '2024-04-10',
        'category': 'Игры',
        'tags': ['games', 'repack', 'rus', 'eng', 'rpg', 'action', 'scifi', '18+'],
        'magnet_link': 'magnet:?xt=urn:btih:example3',
        'quality': 'PC',
        'language': 'Мультиязычный',
    },
    {
        'id': '4',
        'name': 'Oppenheimer / Оппенгеймер (2023) BDRip 4K | Remux | HDR | MVO',
        'size': '62.1 GB',
        'seeds': 987,
        'leechers': 189,
        'downloads': 18900,
        'upload_date': '2024-01-25',
        'category': 'Фильмы',
        'tags': ['movies', '4k', 'hdr', 'remux', 'bdrip', 'multi', 'drama', 'thriller', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example4',
        'quality': '4K HDR Remux',
        'language': 'Мультиязычный',
    },
    {
        'id': '5',
        'name': "Baldur's Gate 3 (2024) PC | v4.1.1 | RePack",
        'size': '92.5 GB',
        'seeds': 2341,
        'leechers': 567,
        'downloads': 45200,
        'upload_date': '2024-03-05',
        'category': 'Игры',
        'tags': ['games', 'repack', 'rus', 'eng', 'rpg', 'fantasy', 'strategy', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example5',
        'quality': 'PC',
        'language': 'Мультиязычный',
    },
    {
        'id': '6',
        'name': 'Attack on Titan / Атака титанов (2024) BDRip 1080p | AniLibria',
        'size': '18.4 GB',
        'seeds': 1876,
        'leechers': 234,
        'downloads': 28700,
        'upload_date': '2024-07-01',
        'category': 'Аниме',
        'tags': ['anime', '1080p', 'bdrip', 'rus', 'action', 'drama', 'fantasy', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example6',
        'quality': '1080p',
        'language': 'Русский (AniLibria)',
    },
    {
        'id': '7',
        'name': 'Planet Earth III / Планета Земля 3 (2024) BDRip 4K | HDR | DUB',
        'size': '78.9 GB',
        'seeds': 654,
        'leechers': 123,
        'downloads': 9800,
        'upload_date': '2024-02-14',
        'category': 'Документальные',
        'tags': ['documentary', '4k', 'hdr', 'bdrip', 'rus', 'eng', '0+'],
        'magnet_link': 'magnet:?xt=urn:btih:example7',
        'quality': '4K HDR',
        'language': 'Русский (дубляж)',
    },
    {
        'id': '8',
        'name': 'Adobe Photoshop 2024 v25.12 [x64] RePack',
        'size': '3.2 GB',
        'seeds': 3421,
        'leechers': 890,
        'downloads': 67800,
        'upload_date': '2024-06-01',
        'category': 'Программы',
        'tags': ['software', 'repack', 'rus', 'eng', '0+'],
        'magnet_link': 'magnet:?xt=urn:btih:example8',
        'quality': 'x64',
        'language': 'Мультиязычный',
    },
    {
        'id': '9',
        'name': 'The Witcher / Ведьмак (2024) S03 WEB-DL 1080p | Netflix',
        'size': '28.6 GB',
        'seeds': 1234,
        'leechers': 345,
        'downloads': 22100,
        'upload_date': '2024-04-25',
        'category': 'Сериалы',
        'tags': ['series', '1080p', 'webdl', 'rus', 'eng', 'fantasy', 'action', 'drama', '18+'],
        'magnet_link': 'magnet:?xt=urn:btih:example9',
        'quality': '1080p',
        'language': 'Мультиязычный',
    },
    {
        'id': '10',
        'name': 'Мастер и Маргарита (2024) BDRip 1080p | DUB',
        'size': '14.7 GB',
        'seeds': 876,
        'leechers': 198,
        'downloads': 13400,
        'upload_date': '2024-03-18',
        'category': 'Фильмы',
        'tags': ['movies', '1080p', 'bdrip', 'rus', 'drama', 'fantasy', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example10',
        'quality': '1080p',
        'language': 'Русский (дубляж)',
    },
    {
        'id': '11',
        'name': 'Elden Ring: Shadow of the Erdtree DLC (2024) PC | RePack',
        'size': '48.2 GB',
        'seeds': 1567,
        'leechers': 432,
        'downloads': 29800,
        'upload_date': '2024-06-21',
        'category': 'Игры',
        'tags': ['games', 'repack', 'rus', 'eng', 'rpg', 'action', 'fantasy', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example11',
        'quality': 'PC',
        'language': 'Мультиязычный',
    },
    {
        'id': '12',
        'name': 'Jujutsu Kaisen / Магическая битва (2024) BDRip 1080p | AniDUB',
        'size': '12.3 GB',
        'seeds': 1432,
        'leechers': 287,
        'downloads': 19500,
        'upload_date': '2024-05-10',
        'category': 'Аниме',
        'tags': ['anime', '1080p', 'bdrip', 'rus', 'action', 'fantasy', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example12',
        'quality': '1080p',
        'language': 'Русский (AniDUB)',
    },
    {
        'id': '13',
        'name': 'Windows 11 Pro 24H2 Build 26100 [x64] Activated',
        'size': '5.4 GB',
        'seeds': 4532,
        'leechers': 1234,
        'downloads': 89000,
        'upload_date': '2024-07-05',
        'category': 'Программы',
        'tags': ['software', 'rus', 'eng', '0+'],
        'magnet_link': 'magnet:?xt=urn:btih:example13',
        'quality': 'x64',
        'language': 'Мультиязычный',
    },
    {
        'id': '14',
        'name': 'Fallout (2024) S01 WEB-DL 2160p 4K | HDR | DUB | Amazon',
        'size': '56.8 GB',
        'seeds': 1876,
        'leechers': 432,
        'downloads': 34500,
        'upload_date': '2024-04-12',
        'category': 'Сериалы',
        'tags': ['series', '4k', 'hdr', 'webdl', 'rus', 'scifi', 'action', 'drama', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example14',
        'quality': '4K HDR',
        'language': 'Русский (дубляж)',
    },
    {
        'id': '15',
        'name': 'Довод / Tenet (2020) UHD BDRemux 2160p | 4K | HDR | DUB',
        'size': '54.3 GB',
        'seeds': 765,
        'leechers': 145,
        'downloads': 11200,
        'upload_date': '2024-01-08',
        'category': 'Фильмы',
        'tags': ['movies', '4k', 'hdr', 'remux', 'rus', 'action', 'scifi', 'thriller', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example15',
        'quality': '4K HDR Remux',
        'language': 'Русский (дубляж)',
    },
    {
        'id': '16',
        'name': 'Helldivers 2 (2024) PC | v1.000.301 | RePack',
        'size': '35.6 GB',
        'seeds': 2100,
        'leechers': 567,
        'downloads': 38900,
        'upload_date': '2024-05-28',
        'category': 'Игры',
        'tags': ['games', 'repack', 'rus', 'eng', 'shooter', 'action', 'scifi', '18+'],
        'magnet_link': 'magnet:?xt=urn:btih:example16',
        'quality': 'PC',
        'language': 'Мультиязычный',
    },
    {
        'id': '17',
        'name': 'One Piece / Ван-Пис (2024) WEB-DL 1080p | AniMedia',
        'size': '2.1 GB',
        'seeds': 987,
        'leechers': 156,
        'downloads': 14300,
        'upload_date': '2024-07-08',
        'category': 'Аниме',
        'tags': ['anime', '1080p', 'webdl', 'rus', 'action', 'comedy', 'fantasy', '12+'],
        'magnet_link': 'magnet:?xt=urn:btih:example17',
        'quality': '1080p',
        'language': 'Русский (AniMedia)',
    },
    {
        'id': '18',
        'name': 'Коллекция Стивена Кинга (50 книг) [FB2/EPUB]',
        'size': '890 MB',
        'seeds': 543,
        'leechers': 78,
        'downloads': 8700,
        'upload_date': '2024-02-28',
        'category': 'Книги',
        'tags': ['books', 'rus', 'horror', 'thriller', 'drama', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example18',
        'quality': 'FB2/EPUB',
        'language': 'Русский',
    },
    {
        'id': '19',
        'name': 'Pink Floyd - Discography (1967-2023) FLAC',
        'size': '12.4 GB',
        'seeds': 876,
        'leechers': 123,
        'downloads': 15600,
        'upload_date': '2024-03-22',
        'category': 'Музыка',
        'tags': ['music', 'eng', '0+'],
        'magnet_link': 'magnet:?xt=urn:btih:example19',
        'quality': 'FLAC',
        'language': 'Английский',
    },
    {
        'id': '20',
        'name': 'Гладиатор 2 / Gladiator II (2024) CAM-Rip 720p | DUB',
        'size': '3.8 GB',
        'seeds': 4321,
        'leechers': 876,
        'downloads': 56700,
        'upload_date': '2024-07-10',
        'category': 'Фильмы',
        'tags': ['movies', '720p', 'rus', 'action', 'drama', '16+'],
        'magnet_link': 'magnet:?xt=urn:btih:example20',
        'quality': '720p',
        'language': 'Русский (дубляж)',
    },
]

# Теги
tags_data = [
    # Категории
    {'id': 'movies', 'name': 'Фильмы', 'category': 'Категория', 'color': 'bg-red-500'},
    {'id': 'series', 'name': 'Сериалы', 'category': 'Категория', 'color': 'bg-orange-500'},
    {'id': 'games', 'name': 'Игры', 'category': 'Категория', 'color': 'bg-green-500'},
    {'id': 'music', 'name': 'Музыка', 'category': 'Категория', 'color': 'bg-purple-500'},
    {'id': 'software', 'name': 'Программы', 'category': 'Категория', 'color': 'bg-blue-500'},
    {'id': 'books', 'name': 'Книги', 'category': 'Категория', 'color': 'bg-yellow-600'},
    {'id': 'anime', 'name': 'Аниме', 'category': 'Категория', 'color': 'bg-pink-500'},
    {'id': 'documentary', 'name': 'Документальные', 'category': 'Категория', 'color': 'bg-teal-500'},
    
    # Качество видео
    {'id': '4k', 'name': '4K', 'category': 'Качество', 'color': 'bg-indigo-500'},
    {'id': '1080p', 'name': '1080p', 'category': 'Качество', 'color': 'bg-indigo-400'},
    {'id': '720p', 'name': '720p', 'category': 'Качество', 'color': 'bg-indigo-300'},
    {'id': 'hdr', 'name': 'HDR', 'category': 'Качество', 'color': 'bg-violet-500'},
    
    # Языки
    {'id': 'rus', 'name': 'Русский', 'category': 'Язык', 'color': 'bg-sky-500'},
    {'id': 'eng', 'name': 'Английский', 'category': 'Язык', 'color': 'bg-sky-400'},
    {'id': 'multi', 'name': 'Мультиязычный', 'category': 'Язык', 'color': 'bg-sky-300'},
    
    # Жанры
    {'id': 'action', 'name': 'Боевик', 'category': 'Жанр', 'color': 'bg-rose-500'},
    {'id': 'comedy', 'name': 'Комедия', 'category': 'Жанр', 'color': 'bg-amber-500'},
    {'id': 'drama', 'name': 'Драма', 'category': 'Жанр', 'color': 'bg-slate-500'},
    {'id': 'horror', 'name': 'Ужасы', 'category': 'Жанр', 'color': 'bg-gray-700'},
    {'id': 'scifi', 'name': 'Фантастика', 'category': 'Жанр', 'color': 'bg-cyan-500'},
    {'id': 'thriller', 'name': 'Триллер', 'category': 'Жанр', 'color': 'bg-stone-600'},
    {'id': 'fantasy', 'name': 'Фэнтези', 'category': 'Жанр', 'color': 'bg-emerald-500'},
    {'id': 'rpg', 'name': 'RPG', 'category': 'Жанр', 'color': 'bg-emerald-400'},
    {'id': 'strategy', 'name': 'Стратегия', 'category': 'Жанр', 'color': 'bg-lime-500'},
    {'id': 'shooter', 'name': 'Шутер', 'category': 'Жанр', 'color': 'bg-red-600'},
    
    # Тип
    {'id': 'remux', 'name': 'Remux', 'category': 'Тип', 'color': 'bg-fuchsia-500'},
    {'id': 'webdl', 'name': 'WEB-DL', 'category': 'Тип', 'color': 'bg-fuchsia-400'},
    {'id': 'bdrip', 'name': 'BDRip', 'category': 'Тип', 'color': 'bg-fuchsia-300'},
    {'id': 'dvdrip', 'name': 'DVDRip', 'category': 'Тип', 'color': 'bg-fuchsia-200'},
    {'id': 'repack', 'name': 'Repack', 'category': 'Тип', 'color': 'bg-pink-400'},
    
    # Возрастные ограничения
    {'id': '18+', 'name': '18+', 'category': 'Возраст', 'color': 'bg-red-700'},
    {'id': '16+', 'name': '16+', 'category': 'Возраст', 'color': 'bg-orange-600'},
    {'id': '12+', 'name': '12+', 'category': 'Возраст', 'color': 'bg-yellow-500'},
    {'id': '6+', 'name': '6+', 'category': 'Возраст', 'color': 'bg-green-500'},
    {'id': '0+', 'name': '0+', 'category': 'Возраст', 'color': 'bg-blue-500'},
]

tag_categories = ['Категория', 'Качество', 'Язык', 'Жанр', 'Тип', 'Возраст']

@app.route('/')
def index():
    # Получаем параметры запроса
    search_query = request.args.get('search', '').strip()
    selected_tags = request.args.getlist('tags')
    sort_by = request.args.get('sort', 'seeds')
    
    # Фильтрация
    filtered_torrents = torrents_data.copy()
    
    # Фильтр по поисковому запросу
    if search_query:
        query_lower = search_query.lower()
        filtered_torrents = [
            t for t in filtered_torrents
            if query_lower in t['name'].lower() or
               query_lower in t['category'].lower() or
               any(query_lower in tags_data[i]['name'].lower() 
                   for i, tag in enumerate(t['tags']) 
                   if any(td['id'] == tag for td in tags_data))
        ]
    
    # Фильтр по тегам
    if selected_tags:
        filtered_torrents = [
            t for t in filtered_torrents
            if all(tag in t['tags'] for tag in selected_tags)
        ]
    
    # Сортировка
    if sort_by == 'seeds':
        filtered_torrents.sort(key=lambda x: x['seeds'], reverse=True)
    elif sort_by == 'downloads':
        filtered_torrents.sort(key=lambda x: x['downloads'], reverse=True)
    elif sort_by == 'date':
        filtered_torrents.sort(key=lambda x: datetime.strptime(x['upload_date'], '%Y-%m-%d'), reverse=True)
    
    return render_template(
        'index.html',
        torrents=filtered_torrents,
        tags=tags_data,
        tag_categories=tag_categories,
        search_query=search_query,
        selected_tags=selected_tags,
        sort_by=sort_by,
        total_torrents=len(torrents_data)
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
