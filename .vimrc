"
"---------------------------
" Start Neobundle Settings.
"---------------------------
" bundleで管理するディレクトリを指定
set runtimepath+=~/.vim/bundle/neobundle.vim/

" Required:
call neobundle#begin(expand('~/.vim/bundle/'))

"neobundle自体をneobundleで管理
NeoBundleFetch 'Shougo/neobundle.vim'

"以下追加plugin
NeoBundle "ompugao/ros.vim"
NeoBundle 'scrooloose/nerdcommenter'
NeoBundle 'yegappan/mru'
NeoBundle 'Townk/vim-autoclose'
NeoBundle 'junegunn/vim-easy-align'
NeoBundle 'SingleCompile'

call neobundle#end()

" Required:
filetype plugin indent on

" 未インストールのプラグインがある場合、インストールするかどうかを尋ねてくれるようにする設定
" 毎回聞かれると邪魔な場合もあるので、この設定は任意です。
" NeoBundleCheck

"-------------------------
" End Neobundle Settings.
"-------------------------
"
"カッコ系とかクォート系を入力したときに、自動的に閉じてくれるコマンド"
" inoremap { {}<LEFT>
" inoremap [ []<LEFT>
" inoremap ( ()<LEFT>
" inoremap " ""<LEFT>
" inoremap "" ""
" inoremap ' ''<LEFT>
" vnoremap { "zdi^V{<C-R>z}<ESC>
" vnoremap [ "zdi^V[<C-R>z]<ESC>
" vnoremap ( "zdi^V(<C-R>z)<ESC>

" vnoremap " "zdi^V"<C-R>z^V"<ESC>
" vnoremap ' "zdi'<C-R>z'<ESC>


set number "行番号を表示する
set title "編集中のファイル名を表示
set showmatch "括弧入力時の対応する括弧を表示
set cursorline
highlight CursorLine cterm=NONE ctermfg=NONE ctermbg=black
highlight Normal ctermfg=grey
syntax on "コードの色分け
set tabstop=4 "インデントをスペース4つ分に設定
set shiftwidth=4
set autoindent
set smartindent "オートインデント
augroup fileTypeIndent
    autocmd!
    autocmd BufNewFile,BufRead *.py setlocal expandtab
augroup END
"#####検索設定#####
set ignorecase "大文字/小文字の区別なく検索する
set smartcase "検索文字列に大文字が含まれている場合は区別して検索する
set wrapscan "検索時に最後まで行ったら最初に戻る
set noswapfile

" set clipboard=unnamedplus "OS のクリップボードと vim のヤンクを共有する．
set clipboard=autoselect,unnamedplus
"source ~/.vim/script/RosTopicList.vim

"nerdcommenter用 cc でコメントor コメントアウト
let NERDSpaceDelims = 1
nmap cc <Plug>NERDCommenterToggle
vmap cc <Plug>NERDCommenterToggle
"mru用 スペース2回押しでプラグイン起動
nnoremap <space><space> :<c-u>MRU<CR>

"自動整形プラグイン用 整形したい部分をvisual modeで選択してenter.
" Start interactive EasyAlign in visual mode (e.g. vip<Enter>)
vmap <Enter> <Plug>(EasyAlign)
" Start interactive EasyAlign for a motion/text object (e.g.<Leader>aip)
nmap <Leader>a <Plug>(EasyAlign)

"DoxygenToolkitは C/C++ の関数の先頭で :Dox とうつと，自動的に
"Doxygenスタイルのコメントを挿入してくれる．
"
"vim-autoclose はカッコのケツを自動挿入してくれる．
"
"nerdtree は :NERDTree でディレクトリツリーの表示．

"original"
" set cursorline
" highlight CursorLine cterm=NONE ctermfg=NONE ctermbg=black
"change line
set hlsearch
nmap <CR> i<CR><ESC>
nnoremap <Space>w :w<Enter>
nnoremap <Space>q :q<Enter>
nnoremap <Space>m :make<Enter>
nnoremap <Space>t :tabnew
nnoremap <F5> :!python %<Enter>

inoremap jj <ESC><Right>
nnoremap <C-h> :noh<CR>

set undodir=$HOME/.vim/.vimundo
set undofile

set wildmode=longest,list

"カラースキームの設定"
set t_Co=256
" set t_Co=16

" hybrid"
set background=dark
colorscheme hybrid

" tender"
" colorscheme tender

" molokai"
" colorscheme molokai

"wombat256mod"
" colorscheme wombat256mod

"jellybeans"
" colorscheme jellybeans

"gruvbox"
" set background=dark
" colorscheme gruvbox

"Smyck"
" set background=dark
" colorscheme smyck

"spacegray "
" colorscheme spacegray

"solarized "
" set background=dark
" colorscheme solarized

"base_16-default-dark"
" colorscheme base16-default-dark
"
"badwolf "
" set background=dark
" colorscheme badwolf

"atom-dark "
" colorscheme atom-dark-256

"eva01"
" colorscheme eva01

"1989"
" colorscheme 1989

"Tomorrow-Night-Bright"
" colorscheme Tomorrow-Night-Bright

"Tomorrow-Night"
" colorscheme Tomorrow-Night

" railscasts"
" colorscheme railscasts

" papercolor"
" set background=dark
" colorscheme PaperColor

" pencil"
" set background=dark
" colorscheme pencil

" minimalist"
" colorscheme minimalist
