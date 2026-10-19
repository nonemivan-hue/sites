import { useState, useMemo } from 'react';
import { Search, Filter, Download, X, Tag, TrendingUp, Clock, HardDrive } from 'lucide-react';
import { torrents, tags, tagCategories, Torrent } from './data/torrents';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedTags, setSelectedTags] = useState<string[]>([]);
  const [sortBy, setSortBy] = useState<'seeds' | 'downloads' | 'date'>('seeds');
  const [expandedCategories, setExpandedCategories] = useState<string[]>(['Категория']);
  const [showFilters, setShowFilters] = useState(true);

  const toggleTag = (tagId: string) => {
    setSelectedTags(prev =>
      prev.includes(tagId)
        ? prev.filter(t => t !== tagId)
        : [...prev, tagId]
    );
  };

  const toggleCategory = (category: string) => {
    setExpandedCategories(prev =>
      prev.includes(category)
        ? prev.filter(c => c !== category)
        : [...prev, category]
    );
  };

  const filteredTorrents = useMemo(() => {
    let result = torrents;

    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase();
      result = result.filter(t =>
        t.name.toLowerCase().includes(query) ||
        t.category.toLowerCase().includes(query) ||
        t.tags.some(tag => {
          const tagData = tags.find(tg => tg.id === tag);
          return tagData?.name.toLowerCase().includes(query);
        })
      );
    }

    if (selectedTags.length > 0) {
      result = result.filter(torrent =>
        selectedTags.every(tag => torrent.tags.includes(tag))
      );
    }

    result = [...result].sort((a, b) => {
      switch (sortBy) {
        case 'seeds':
          return b.seeds - a.seeds;
        case 'downloads':
          return b.downloads - a.downloads;
        case 'date':
          return new Date(b.uploadDate).getTime() - new Date(a.uploadDate).getTime();
        default:
          return 0;
      }
    });

    return result;
  }, [searchQuery, selectedTags, sortBy]);

  const clearFilters = () => {
    setSelectedTags([]);
    setSearchQuery('');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white">
      {/* Header */}
      <header className="border-b border-gray-700/50 bg-gray-900/80 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl flex items-center justify-center">
                <Download className="w-5 h-5 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
                  TorrentFinder
                </h1>
                <p className="text-xs text-gray-400">Поиск торрентов по тегам</p>
              </div>
            </div>
            <div className="flex items-center gap-2 text-sm text-gray-400">
              <HardDrive className="w-4 h-4" />
              <span>{torrents.length} раздач</span>
            </div>
          </div>
        </div>
      </header>

      {/* Search Section */}
      <div className="max-w-7xl mx-auto px-4 py-6">
        <div className="relative">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder="Поиск торрентов по названию, категории или тегам..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-12 pr-4 py-4 bg-gray-800/80 border border-gray-700 rounded-2xl text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500/50 transition-all text-lg"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery('')}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          )}
        </div>

        {selectedTags.length > 0 && (
          <div className="flex flex-wrap items-center gap-2 mt-4">
            <span className="text-sm text-gray-400">Выбрано:</span>
            {selectedTags.map(tagId => {
              const tag = tags.find(t => t.id === tagId);
              if (!tag) return null;
              return (
                <button
                  key={tagId}
                  onClick={() => toggleTag(tagId)}
                  className={`inline-flex items-center gap-1 px-3 py-1 rounded-full text-sm font-medium ${tag.color} text-white hover:opacity-80 transition-opacity`}
                >
                  {tag.name}
                  <X className="w-3 h-3" />
                </button>
              );
            })}
            <button
              onClick={clearFilters}
              className="text-sm text-gray-400 hover:text-white underline transition-colors"
            >
              Сбросить всё
            </button>
          </div>
        )}
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 pb-8">
        <div className="flex flex-col lg:flex-row gap-6">
          {/* Sidebar */}
          <aside className={`lg:w-72 flex-shrink-0 transition-all ${showFilters ? 'block' : 'hidden lg:block'}`}>
            <div className="bg-gray-800/50 border border-gray-700/50 rounded-2xl p-4 sticky top-24">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-lg font-semibold flex items-center gap-2">
                  <Filter className="w-5 h-5 text-purple-400" />
                  Теги
                </h2>
                <button
                  onClick={() => setShowFilters(!showFilters)}
                  className="lg:hidden text-gray-400 hover:text-white"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <div className="space-y-3 max-h-[calc(100vh-200px)] overflow-y-auto pr-1">
                {tagCategories.map(category => (
                  <div key={category}>
                    <button
                      onClick={() => toggleCategory(category)}
                      className="w-full flex items-center justify-between py-2 px-2 rounded-lg hover:bg-gray-700/50 transition-colors text-left"
                    >
                      <span className="text-sm font-medium text-gray-300">{category}</span>
                      <span className="text-xs text-gray-500">
                        {expandedCategories.includes(category) ? '▼' : '▶'}
                      </span>
                    </button>
                    {expandedCategories.includes(category) && (
                      <div className="flex flex-wrap gap-1.5 mt-2 mb-2 pl-2">
                        {tags
                          .filter(tag => tag.category === category)
                          .map(tag => (
                            <button
                              key={tag.id}
                              onClick={() => toggleTag(tag.id)}
                              className={`px-2.5 py-1 rounded-lg text-xs font-medium transition-all ${
                                selectedTags.includes(tag.id)
                                  ? `${tag.color} text-white shadow-lg scale-105`
                                  : 'bg-gray-700/50 text-gray-300 hover:bg-gray-600/50'
                              }`}
                            >
                              {tag.name}
                            </button>
                          ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </aside>

          {/* Results */}
          <main className="flex-1 min-w-0">
            <div className="flex items-center justify-between mb-4">
              <p className="text-sm text-gray-400">
                Найдено: <span className="text-white font-medium">{filteredTorrents.length}</span> раздач
              </p>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setShowFilters(!showFilters)}
                  className="lg:hidden flex items-center gap-1 px-3 py-1.5 bg-gray-800 border border-gray-700 rounded-lg text-sm text-gray-300 hover:text-white transition-colors"
                >
                  <Filter className="w-4 h-4" />
                  Теги
                </button>
                <div className="flex items-center gap-1 bg-gray-800 border border-gray-700 rounded-lg p-1">
                  <button
                    onClick={() => setSortBy('seeds')}
                    className={`flex items-center gap-1 px-3 py-1 rounded-md text-xs font-medium transition-all ${
                      sortBy === 'seeds' ? 'bg-purple-500/20 text-purple-300' : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    <TrendingUp className="w-3 h-3" />
                    Сиды
                  </button>
                  <button
                    onClick={() => setSortBy('downloads')}
                    className={`flex items-center gap-1 px-3 py-1 rounded-md text-xs font-medium transition-all ${
                      sortBy === 'downloads' ? 'bg-purple-500/20 text-purple-300' : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    <Download className="w-3 h-3" />
                    Загрузки
                  </button>
                  <button
                    onClick={() => setSortBy('date')}
                    className={`flex items-center gap-1 px-3 py-1 rounded-md text-xs font-medium transition-all ${
                      sortBy === 'date' ? 'bg-purple-500/20 text-purple-300' : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    <Clock className="w-3 h-3" />
                    Дата
                  </button>
                </div>
              </div>
            </div>

            <div className="space-y-3">
              {filteredTorrents.length === 0 ? (
                <div className="text-center py-16">
                  <div className="w-20 h-20 mx-auto mb-4 bg-gray-800 rounded-full flex items-center justify-center">
                    <Search className="w-8 h-8 text-gray-600" />
                  </div>
                  <h3 className="text-lg font-medium text-gray-400 mb-2">Ничего не найдено</h3>
                  <p className="text-sm text-gray-500">Попробуйте изменить параметры поиска или сбросить фильтры</p>
                  <button
                    onClick={clearFilters}
                    className="mt-4 px-4 py-2 bg-purple-500/20 text-purple-300 rounded-lg hover:bg-purple-500/30 transition-colors"
                  >
                    Сбросить фильтры
                  </button>
                </div>
              ) : (
                filteredTorrents.map(torrent => (
                  <TorrentCard key={torrent.id} torrent={torrent} />
                ))
              )}
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}

function TorrentCard({ torrent }: { torrent: Torrent }) {
  const [copied, setCopied] = useState(false);

  const handleCopyMagnet = () => {
    navigator.clipboard.writeText(torrent.magnetLink).catch(() => {});
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short', year: 'numeric' });
  };

  return (
    <div className="bg-gray-800/50 border border-gray-700/50 rounded-xl p-4 hover:border-purple-500/30 hover:bg-gray-800/70 transition-all group">
      <div className="flex flex-col sm:flex-row sm:items-start gap-3">
        <div className="flex-shrink-0">
          <span className={`inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-bold ${
            torrent.category === 'Фильмы' ? 'bg-red-500/20 text-red-300' :
            torrent.category === 'Сериалы' ? 'bg-orange-500/20 text-orange-300' :
            torrent.category === 'Игры' ? 'bg-green-500/20 text-green-300' :
            torrent.category === 'Музыка' ? 'bg-purple-500/20 text-purple-300' :
            torrent.category === 'Программы' ? 'bg-blue-500/20 text-blue-300' :
            torrent.category === 'Книги' ? 'bg-yellow-500/20 text-yellow-300' :
            torrent.category === 'Аниме' ? 'bg-pink-500/20 text-pink-300' :
            'bg-teal-500/20 text-teal-300'
          }`}>
            {torrent.category}
          </span>
        </div>

        <div className="flex-1 min-w-0">
          <h3 className="text-sm sm:text-base font-medium text-white group-hover:text-purple-300 transition-colors leading-snug mb-2">
            {torrent.name}
          </h3>

          <div className="flex flex-wrap gap-1 mb-3">
            {torrent.tags.slice(0, 5).map(tagId => {
              const tag = tags.find(t => t.id === tagId);
              if (!tag) return null;
              return (
                <span
                  key={tagId}
                  className="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-gray-700/30 text-gray-300 border border-gray-600/50"
                >
                  <Tag className="w-2.5 h-2.5 mr-1" />
                  {tag.name}
                </span>
              );
            })}
            {torrent.tags.length > 5 && (
              <span className="text-[10px] text-gray-500 px-2 py-0.5">
                +{torrent.tags.length - 5}
              </span>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-gray-400">
            <span className="flex items-center gap-1">
              <HardDrive className="w-3 h-3" />
              {torrent.size}
            </span>
            <span className="flex items-center gap-1 text-green-400">
              <TrendingUp className="w-3 h-3" />
              {torrent.seeds.toLocaleString()} сидов
            </span>
            <span className="flex items-center gap-1 text-red-400">
              {torrent.leechers.toLocaleString()} личей
            </span>
            <span className="flex items-center gap-1">
              <Download className="w-3 h-3" />
              {torrent.downloads.toLocaleString()}
            </span>
            <span className="flex items-center gap-1">
              <Clock className="w-3 h-3" />
              {formatDate(torrent.uploadDate)}
            </span>
          </div>
        </div>

        <div className="flex-shrink-0 flex sm:flex-col items-center gap-2">
          <button
            onClick={handleCopyMagnet}
            className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-all ${
              copied
                ? 'bg-green-500/20 text-green-300 border border-green-500/30'
                : 'bg-purple-500/20 text-purple-300 border border-purple-500/30 hover:bg-purple-500/30'
            }`}
          >
            {copied ? (
              <>✓ Скопировано</>
            ) : (
              <>
                <Download className="w-4 h-4" />
                Magnet
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
