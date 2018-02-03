import math
import numpy as np
import uservectors

import twitter

api = twitter.Twitter(auth = twitter.OAuth(consumer_key='gafkoAHgzhezUbu03gQ1LWG5N',
                  consumer_secret='WeSTTsNKYAoqyt5HqNCMgqy4cdkUlaA0lIhaWggdORpEgXsON6',
                token='2319318205-dMtFoL3Ge8oVOn7dLYp7PbSqdLkuXx4cYBvfllW',
                  token_secret='p8oCn4YLsgwwaUDmsPWzBHVeGKean6j7svuYEcTtxboSZ'))

from nltk.tokenize import word_tokenize
print('imported tokenize')
import re
print('imported re')

knowns = ['!', '#', '$', '%', '&', "'", "''", "'ll", "'m", "'re", "'s", "'ve", '(', ')', ',', '-', '--', '-and', '-galileo', '.', '..', '...', '/', '//t.co/axkaiqkufz', '//t.co/gr3opncao4', '//t.co/gr3opnubfc', '//t.co/j9wllbcy7d', '//t.co/me5khrvp4j', '//t.co/nm32bzchvq', '//t.co/oa6vvmjtcu', '//t.co/pta1gki68y', '//t.co/pta1gkqujy', '//t.co/qw885kfek2', '//t.co/usxik9phqc', '//t.co/usxika7iom', '//t.co/\u2026', '//t.c\u2026', '//t.\u2026', '//t\u2026', '1', '1,000', '1.', '1.2', '10', '1000', '11', '12', '13', '13th', '14', '15', '16.0', '16.1', '17', '18', '1961', '1st', '2', '2,000', '2,000,000', '20', '2016', '2017', '2018', '2018.', '2019.', '20th', '23', '25,000', '25,000.', '26', '28', '2nd', '3', '30', '39a', '3rd', '3x', '4', '4.1', '40', '45', '49', '5', '50', '50,000', '51', '59', '5th', '6', '8', '89blocks', '9', '9.8.17', '9am', ':', ';', '?', '@', '[', ']', '``', 'a', 'able', 'about', 'access', 'accomplishments', 'account', 'accumulate', 'accurate', 'across', 'act', 'action', 'actually', 'add', 'added', 'addiction', 'address', 'adds', 'administration', 'advanced', 'af', 'african', 'after', 'again', 'against', 'agenda', 'ago', 'agree', 'agreed', 'ahead', 'ai', 'ain', 'air', 'aka', 'akron', 'alabama', 'album', 'alec_ksiazek', 'alex', 'alien', 'aliens', 'all', 'allow', 'allowed', 'almost', 'already', 'also', 'always', 'am', 'amas', 'amazing', 'america', 'american', 'americans', 'among', 'amounts', 'amp', 'an', 'and', 'announce', 'announced', 'announcing', 'annual', 'another', 'answers', 'antiversary', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'apocalypse', 'apollo', 'apparently', 'apple', 'applepodcasts', 'appreciate', 'appropriate', 'approval', 'are', 'aren', 'around', 'article', 'as', 'asahdkhaled', 'ascent', 'asked', 'ass', 'astronomical', 'astrophysics', 'at', 'auntumn', 'australian', 'author', 'authorization', 'autumn', 'available', 'avaschiffer', 'aw17', 'awards', 'away', 'awesome', 'back', 'backwards', 'bad', 'badly', 'ball', 'band', 'bannon', 'bars', 'base', 'based', 'basketball', 'bday', 'be', 'beating', 'beautiful', 'beauty', 'because', 'become', 'been', 'before', 'behalf', 'behind', 'being', 'believe', 'below', 'benefits', 'benjamin', 'best', 'bet', 'better', 'between', 'beyond', 'biased', 'big', 'bigger', 'biggest', 'bilateral', 'bill', 'billboard', 'billion', 'billions', 'billnye', 'bipartisan', 'birds', 'birthday', 'black', 'blame', 'blazepizza', 'blessed', 'blow', 'blowing', 'blue', 'bob', 'bomb', 'bonuses', 'boogiecousins', 'book', 'books', 'booming', 'booster', 'border', 'borders', 'boring', 'boringcompany', 'both', 'bottle', 'bout', 'brand', 'brave', 'breath', 'bring', 'bringing', 'bro', 'broken', 'brother', 'budget', 'build', 'built', 'bulldogs', 'bunch', 'business', 'businesses', 'but', 'button', 'buy', 'by', 'ca', 'cabinet', 'calendar', 'call', 'called', 'calling', 'calm', 'campaign', 'can', 'cap', 'capacity', 'cape', 'capsule', 'car', 'care', 'caribbean', 'carmeloanthony', 'cars', 'case', 'cassini', 'cast', 'cat', 'catch', 'cave', 'celebrate', 'center', 'certain', 'certainly', 'chain', 'chance', 'chandlerriggs', 'change', 'channing_frye', 'characters', 'charity', 'chase', 'check', 'chicago', 'chill', 'christmas', 'chrysler', 'chuck', 'chucknicecomic', 'cities', 'city', 'civilian', 'claralionelfdn', 'class', 'clear', 'cleated', 'clf', 'clinton', 'close', 'closer', 'cnn', 'coins', 'cold', 'colleagues', 'collection', 'collusion', 'colors', 'come', 'comes', 'coming', 'comment', 'commission', 'commit', 'commitment', 'committee', 'communities', 'community', 'companies', 'company', 'compared', 'complete', 'completely', 'composite', 'conceal', 'concerned', 'conference', 'congrats', 'congratulations', 'congress', 'conservative', 'construct', 'contact', 'continue', 'continues', 'contour', 'control', 'cool', 'core', 'cores', 'correct', 'corrupt', 'cosmic', 'cosmically', 'cosmos', 'could', 'couldn', 'country', 'course', 'court', 'cover', 'coverage', 'covering', 'covers', 'cp3', 'crazy', 'created', 'creating', 'credit', 'creeper', 'crew', 'crime', 'cristatolive', 'crooked', 'cryin', 'current', 'customs', 'cut', 'cuts', 'cutting', 'd', 'd.', 'da', 'daca', 'dakar', 'damn', 'dance', 'dangerous', 'daniellefong', 'danshedd', 'dat', 'data', 'david', 'davos', 'day', 'days', 'dazed', 'dead', 'deal', 'deals', 'dear', 'death', 'dec', 'dec.', 'dec.26', 'decades', 'decision', 'deep', 'deeply', 'definitely', 'deliver', 'delivery', 'dem', 'demand', 'democrat', 'democratic', 'democrats', 'dems', 'deserves', 'desire', 'desperately', 'despite', 'devastating', 'diamondball', 'dianne', 'dick', 'dicky', 'did', 'didn', 'die', 'different', 'difficult', 'directly', 'director', 'discredited', 'discussing', 'disgrace', 'dishonest', 'dnagtweeter', 'do', 'documentary', 'does', 'doesn', 'dog', 'dogs', 'doing', 'dollar', 'dollars', 'don', 'donald', 'donate', 'done', 'dossier', 'doubling', 'dow', 'down', 'dr.', 'dragon', 'dragons', 'dream', 'drive', 'droneship', 'dropped', 'dropping', 'drops', 'drug', 'drugs', 'duckie_thot', 'dumped', 'duo', 'durbin', 'during', 'dwyanewade', 'dying', 'each', 'early', 'earth', 'easily', 'easter', 'easy', 'eclipse', 'economic', 'economy', 'ed', 'edition', 'education', 'egg', 'elected', 'election', 'electric', 'elephant', 'ellemagazine', 'elonmusk', 'else', 'em', 'emmanuelmacron', 'emphasis', 'employees', 'end', 'endlessly', 'enjoy', 'enough', 'ensure', 'entire', 'equator', 'eric', 'erictrump', 'erna_solberg', 'especially', 'essay', 'est', 'et', 'etc', 'even', 'event', 'events', 'ever', 'every', 'everybody', 'everyone', 'everything', 'evidence', 'exactly', 'excellent', 'excited', 'exciting', 'exclusive', 'exist', 'expand', 'experience', 'experts', 'exploration', 'explores', 'extension', 'extremely', 'eyes', 'eyeshadow', 'f.u', 'fact', 'factory', 'facts', 'failed', 'fake', 'falcon', 'fall', 'false', 'falsely', 'fam', 'families', 'family', 'fan', 'fans', 'fantastic', 'far', 'farmers', 'fashion', 'fast', 'faster', 'father', 'fauna', 'favor', 'favorite', 'fbi', 'features', 'featuring', 'federal', 'feel', 'feeling', 'feinstein', 'female', 'fenty', 'fentybeauty', 'fentyface', 'fentyxpuma', 'few', 'field', 'fight', 'fighting', 'figured', 'filled', 'film', 'films', 'filt', 'final', 'finally', 'find', 'fired', 'firing', 'firm', 'first', 'fisa', 'fit', 'five', 'fix', 'fixed', 'flag', 'flamethrower', 'flamethrowers', 'flatearthorg', 'flight', 'flora', 'florida', 'flying', 'focus', 'follow', 'food', 'for', 'foreign', 'forgot', 'forgotten', 'form', 'forward', 'fought', 'found', 'foundation', 'four', 'fox', 'foxandfriends', 'foxnews', 'foxtv', 'fragrance', 'france', 'franke', 'fredericlambert', 'free', 'friday', 'fridaythe13th', 'friend', 'friends', 'from', 'from\u2026', 'full', 'fully', 'fun', 'fund', 'fundeducation', 'funding', 'further', 'fusion', 'future', 'fyi', 'g', 'galaxy', 'galaxycollection', 'game', 'gameofthrones', 'gang', 'gave', 'gday', 'generally', 'generation', 'genetically', 'genius', 'get', 'getting', 'giant', 'gift', 'girls', 'give', 'given', 'glad', 'glblctzn', 'global', 'gloss', 'go', 'god', 'goes', 'going', 'goirish\u2618\ufe0f', 'gon', 'gone', 'good', 'good.', 'got', 'government', 'govsat-1', 'gpforeducation', 'gps', 'gqmagazine', 'great', 'greatest', 'gregorian', 'gregory', 'ground', 'grow', 'growing', 'gt', 'guaranteed', 'guest', 'guy', 'guys', 'h.r', 'h2o', 'had', 'haiti', 'haitians', 'half', 'handing', 'happen', 'happens', 'happy', 'hard', 'harpersbazaarus', 'harveynichols', 'has', 'hat', 'hate', 'hats', 'have', 'having', 'he', 'head', 'heading', 'headline', 'heard', 'heart', 'heavy', 'hell', 'hello', 'help', 'hence', 'her', 'herbiehancock', 'here', 'hey', 'high', 'high-speed', 'higher', 'highest', 'highlight', 'hillary', 'him', 'his', 'historic', 'historical', 'history', 'hit', 'hits', 'hmm', 'ho', 'hoax', 'hogs', 'holding', 'holiday', 'holidays', 'home', 'homie', 'homies', 'honor', 'honored', 'hope', 'hostage', 'hot', 'hours', 'house', 'houston', 'how', 'https', 'huge', 'human', 'humans', 'humantransit', 'hunt', 'hurry', 'hurt', 'hurting', 'hyper-glitz', 'i', 'icegov', 'id_aa_carmack', 'idea', 'identification', 'idiot', 'if', 'illegal', 'imagine', 'immigrants', 'immigration', 'important', 'improve', 'improvement', 'in', 'inch', 'including', 'incredible', 'indeed', 'inflow', 'influence', 'inform', 'infrastructure', 'innocent', 'inside', 'insight', 'inspire', 'instead', 'intel', 'intelligence', 'intended', 'interest', 'interested', 'interview', 'interviewed', 'into', 'invest', 'investing', 'io', 'ipromise', 'irish', 'is', 'isis', 'issa', 'issue', 'it', 'its', 'ivanescobosa', 'james', 'january', 'jcolenc', 'jennylongworth', 'jim', 'jimsonjim', 'job', 'jobs', 'joeraoweather', 'join', 'jong', 'journey', 'jr.', 'july', 'jump', 'jumped', 'june', 'just', 'justice', 'keep', 'keeping', 'kennedy', 'kevinlove', 'key', 'kicks', 'kid', 'kids', 'killawatt', 'killin', 'kim', 'king', 'kingdom', 'kingjames', 'knew', 'know', 'knowledge', 'knows', 'korea', 'la', 'ladies', 'lady', 'lafite', 'land', 'landed', 'landing', 'language', 'large', 'larry', 'last', 'latest', 'laugh', 'launch', 'launching', 'law', 'laws', 'leader', 'leaders', 'learn', 'learned', 'learning', 'least', 'leaving', 'lebron', 'left', 'legacy', 'legend', 'lens', 'less', 'let', 'level', 'lie', 'life', 'light', 'like', 'likely', 'lil', 'limited', 'line', 'link', 'lip', 'lips', 'lipstick', 'list', 'listen', 'lit', 'little', 'live', 'livelaughlove', 'lives', 'ljfamfoundation', 'll', 'local', 'located', 'lol', 'london', 'long', 'longer', 'look', 'looking', 'looks', 'loop', 'loser', 'lost', 'lotb', 'lots', 'lottery', 'loudobbs', 'lovable', 'love', 'loved', 'lovers', 'low', 'lowest', 'loyalty', 'luck', 'lucky', 'luther', 'm', 'machine', 'macys', 'made', 'maga', 'maga\U0001f1fa\U0001f1f8', 'main', 'mainstream', 'major', 'make', 'makeamericagreatagain', 'makes', 'making', 'malawi', 'man', 'manchester', 'many', 'march', 'marchissue', 'mariasalandra', 'mark', 'market', 'mars', 'martian', 'martin', 'mashup', 'massive', 'matchstix', 'mattemoiselle', 'matter', 'mavcarter', 'mavtechie', 'max', 'may', 'maybe', 'mazda', 'me', 'mean', 'meant', 'meanwhile', 'measure', 'media', 'meet', 'meetbubble', 'meeting', 'meetings', 'members', 'memory', 'men', 'mental', 'merit', 'merry', 'mess', 'met', 'meteors', 'methods', 'mexico', 'michael', 'michigan', 'midnight', 'might', 'migration', 'miles', 'military', 'milky', 'million', 'millions', 'mind', 'minister', 'minutes', 'misleading', 'misrepresented', 'missed', 'mission', 'mkbhd', 'model', 'modern', 'moment', 'monday', 'money', 'monster', 'month', 'months', 'mood', 'moon', 'more', 'moredriven', 'morgan', 'morning', 'most', 'mostly', 'mountains', 'move', 'moving', 'much', 'music', 'must', 'my', 'mysteries', "n't", 'na', 'named', 'nancy', 'nasa', 'nashville', 'natgeochannnel', 'nation', 'national', 'natlparkservice', 'navy', 'nazi', 'nbavote', 'near', 'need', 'needed', 'needs', 'neerajka', 'negative', 'net', 'network', 'neural', 'never', 'new', 'news', 'next', 'nice', 'nicklilja', 'night', 'nike', 'no', 'noaa', 'nobody', 'north', 'not', 'note', 'nothing', 'nov', 'nov.', 'novaspivack', 'november', 'now', 'nuclear', 'number', 'numbers', 'nuts', 'nws', 'nyc', 'o', 'obama', 'obstruction', 'obvious', 'obviously', 'oceans8', 'oceans8movie', 'oct', 'oct.', 'october', 'of', 'off', 'offer', 'office', 'officers', 'officially', 'often', 'of\u2026', 'oh', 'ohio', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'online', 'only', 'open', 'opener', 'opportunity', 'opposite', 'option', 'or', 'orbit', 'order', 'orders', 'other', 'others', 'our', 'out', 'over', 'own', 'owners', 'p.s', 'package', 'pad', 'paid', 'paint', 'parih', 'park', 'part', 'parts', 'party', 'pass', 'past', 'paul', 'paulkrugman', 'paulsperry_', 'paying', 'pcampbell21', 'peace', 'peanuts', 'pelosi', 'people', 'per', 'performance', 'perhaps', 'personally', 'phd', 'phone', 'phony', 'photo', 'physics', 'pick', 'picture', 'piece', 'pieterdewit_nz', 'pizza', 'place', 'plan', 'planet', 'planets', 'planning', 'plant', 'played', 'playing', 'plays', 'please', 'pledge', 'plenty', 'point', 'points', 'policies', 'political', 'politics', 'poll', 'polls', 'poor', 'pop', 'possible', 'possibly', 'post', 'posted', 'potential', 'potus', 'pour', 'pouring', 'power', 'powerful', 'prayers', 'praying', 'predicted', 'premieres', 'present', 'presented', 'presidency', 'president', 'pretty', 'previous', 'primary', 'prime', 'prizes', 'probably', 'problem', 'process', 'product', 'production', 'productive', 'profiltr', 'progress', 'progressive', 'promise', 'promised', 'prosperity', 'protect', 'protection', 'proud', 'public', 'puma', 'pumped', 'push', 'put', 'queen', 'queries', 'question', 'quote', 'r', 'racist', 'radio', 'rain', 'raising', 'rally', 'ran', 'random', 'rapidly', 'rare', 'rarely', 'rate', 'rather', 're', 'reader', 'reading', 'ready', 'reagan', 'real', 'realdonaldtrump', 'really', 'reason', 'reasons', 'rebuilding', 'recently', 'record', 'recorded', 'recovery', 'red', 'reentry', 'reference', 'reflecting', 'reform', 'refused', 'regulation', 'regulations', 'relationship', 'relative', 'release', 'released', 'remaining', 'remember', 'replenishment', 'report', 'reported', 'reporters', 'reporting', 'representatives', 'republican', 'republicans', 'require', 'resources', 'respect', 'respected', 'rest', 'restaurant', 'result', 'results', 'reversed', 'rick', 'rid', 'right', 'rihanna', 'rihannaxstance', 'rings', 'roadster', 'roadtrippinpod', 'rock', 'rocket', 'rocnation', 'rolling', 'ronald', 'room', 'rotates', 'rotation', 'round', 'rt', 'run', 'running', 'russia', 'russian', 'rwtw', 's', 's/o', 'sacred', 'sad', 'safe', 'safety', 'said', 'sales', 'same', 'saturn', 'say', 'saying', 'says', 'scenes', 'school', 'schumer', 'science', 'scientific', 'scientifically', 'scientists', 'screaming', 'season', 'second', 'secret', 'security', 'see', 'seeing', 'seem', 'seen', 'semi', 'senate', 'senator', 'senators', 'send', 'senegal', 'sensibly', 'sent', 'sentiment', 'sephora', 'sephorainjcp', 'sephoralovesfentybeauty', 'sept', 'sept.', 'september', 'series', 'seriously', 'service', 'services', 'set', 'setting', 'seven', 'several', 'sfg\U0001f680', 'shade', 'shades', 'shape', 'she', 'sheesh', 'shoe', 'shonrp2', 'shop', 'short', 'shot', 'should', 'show', 'shows', 'shut', 'shutdown', 'shutting', 'side', 'sign', 'signature', 'signed', 'significant', 'similar', 'simple', 'since', 'sinow', 'sir', 'sis', 'skepticism', 'sky', 'slamonline', 'slashdot', 'slides', 'sloppy', 'small', 'smallfoot', 'smart', 'so', 'so-called', 'social', 'software', 'solar', 'sold', 'solution', 'solve', 'solving', 'some', 'somebody', 'someone', 'something', 'sometimes', 'song', 'soon', 'sorry', 'sounds', 'sources', 'south', 'southern', 'space', 'spacex', 'special', 'species', 'speech', 'spending', 'spent', 'spoke', 'sports', 'spring', 'sputnik', 'spy', 'squad', 'ss18', 'st', 'stability', 'stage', 'stand', 'stands', 'star', 'starlit', 'stars', 'start', 'startalk', 'startalkradio', 'started', 'starts', 'state', 'stated', 'statement', 'statements', 'states', 'stay', 'steak', 'step', 'stephanemaraisnails', 'stephen', 'stephenathome', 'stephencurry30', 'steve', 'stewyoungblood', 'still', 'stock', 'stop', 'store', 'stories', 'story', 'stowstudco', 'straight', 'street', 'strength', 'striveforgreatness', 'striveforgreatness\U0001f680', 'strong', 'stronger', 'students', 'study', 'studying', 'stunna', 'stvmathletics', 'subjects', 'succeed', 'success', 'successful', 'such', 'suede', 'summer', 'sun', 'super', 'support', 'sure', 'suv', 'switzerland', 'system', 't', 'table', 'take', 'taken', 'taking', 'taliban', 'talk', 'talked', 'talking', 'talks', 'tardigrade', 'tax', 'taxes', 'team', 'teammates', 'tech', 'technology', 'tell', 'tend', 'term', 'terminated', 'terrible', 'tesla', 'test', 'testimony', 'testing', 'texas', 'than', 'thank', 'thanks', 'thanksgiving', 'that', 'that\u2026', 'the', 'theaters', 'thee', 'their', 'them', 'then', 'there', 'therealutkarsh', 'thesaurus', 'these', 'thewalkingdead', 'they', 'thing', 'things', 'think', 'thinking', 'thinks', 'this', 'thisissandeepg', 'those', 'though', 'thought', 'thoughts', 'thousand', 'thousands', 'three', 'through', 'thru', 'thrust', 'thursday', 'tiamaria68uk', 'til', 'time', 'times', 'to', 'today', 'together', 'told', 'tomorrow', 'tomorrow..', 'tonight', 'tons', 'too', 'took', 'top', 'total', 'totally', 'tough', 'tow', 'toyota', 'trade', 'trailer', 'trainer', 'transit', 'tremendous', 'trillion', 'trip', 'trophy', 'truck', 'true', 'truly', 'trump', 'trust', 'try', 'trying', 'tuesday', 'tuned', 'tunnel', 'turned', 'turning', 'tutorial', 'tweet', 'tweets', 'twelve', 'twitter', 'two', 'u', 'u.s.', 'un', 'unbelievable', 'uncensored', 'unchecked', 'under', 'unemployment', 'unfair', 'uninterrupted', 'united', 'universe', 'university', 'unless', 'unnecessary', 'unprecedented', 'until', 'up', 'update', 'updates', 'upgrade', 'uplifting', 'upward', 'us', 'usa', 'use', 'used', 'usher', 'using', 'v', 'value', 'vanseedbank', 've', 'very', 'veterans', 'victims', 'video', 'view', 'virginia', 'voguearabia', 'vogueparis', 'voice', 'vote', 'voted', 'voter', 'votes', 'voting', 'vs.', 'w', 'w/', 'wait', 'wall', 'want', 'wanted', 'wanting', 'was', 'watch', 'water', 'way', 'wayne_shorter', 'we', 'wearefamily', 'weather', 'week', 'weeks', 'wef', 'wef18', 'weight', 'welcome', 'well', 'went', 'were', 'wh', 'what', 'when', 'where', 'which', 'while', 'white', 'whitehouse', 'who', 'whole', 'why', 'wife', 'wild', 'wildthoughts', 'will', 'willing', 'win', 'winds', 'wine', 'wingfootsclassic', 'wings', 'winning', 'wins', 'wired', 'witch', 'with', 'without', 'women', 'won', 'wonder', 'wonderful', 'word', 'words', 'work', 'workers', 'working', 'works', 'world', 'worlds', 'would', 'wow', 'write', 'written', 'wrong', 'x', 'y', "y'all", 'ya', 'yeah', 'year', 'year.', 'years', 'yes', 'yesterday', 'yet', 'yeti', 'yo', 'you', 'young', 'your', 'yours', 'yup', 'yusefhairnycmakeup', 'zombie', 'zone', '\u2013', '\u2014', '\u2018', '\u2019', '\u201c', '\u201d', '\u2026', '\u2026don', '\u2192', '\u270a\U0001f3fe\U0001f4aa\U0001f3fe\U0001f451', '\u274cake', '\U0001f1eb\U0001f1f7', '\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8\U0001f1fa\U0001f1f8', '\U0001f355', '\U0001f440', '\U0001f440\U0001f440\U0001f440', '\U0001f451', '\U0001f48b', '\U0001f48b\U0001f48b\U0001f48b', '\U0001f525', '\U0001f525\U0001f525\U0001f525\U0001f525', '\U0001f525\U0001f525\U0001f525\U0001f525\U0001f525', '\U0001f622', '\U0001f64f\U0001f3fe', '\U0001f64f\U0001f3fe\u270a\U0001f3fe\U0001f4aa\U0001f3fe\U0001f451', '\U0001f64f\U0001f3fe\U0001f451', '\U0001f64f\U0001f3fe\U0001f4aa\U0001f3fe', '\U0001f64f\U0001f3fe\U0001f4aa\U0001f3fe\U0001f451', '\U0001f64f\U0001f3fe\U0001f64f\U0001f3fe', '\U0001f680', '\U0001f923\U0001f923\U0001f923\U0001f937\U0001f3fe\u200d\u2642\ufe0f', '\U0001f926\U0001f3fe\u200d\u2642\ufe0f', '\U0001f937\U0001f3fd\u200d\u2640\ufe0f', '\U0001f937\U0001f3fe\u200d\u2642\ufe0f']

def get_timeline(username):
    statuses = api.statuses.user_timeline(screen_name = username, tweet_mode = 'extended', count = 200)
    return [status['full_text'].replace('\n','') for status in statuses]

def ngram(corpus, gram_size):
    ngrams = {}
    for i in range(len(corpus) - gram_size + 1):
        ngram = ' '.join(corpus[i:i+gram_size])
        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1
    return ngrams

def flip_dict(d):
    counts = {}
    for word, count in d.items():
        if count in counts:
            counts[count] = counts[count] + [word]
        else:
            counts[count] = [word]
    return counts

def binary_search(key,l):
    low_bound = -1
    high_bound = len(l)
    while True:
        check = (low_bound + high_bound)//2
        if check == low_bound:
            return False
        item = l[check]
        if item == key:
            return True
        elif item < key:
            low_bound = check
        else:
            high_bound = check

def preprocess(text):
    return word_tokenize(re.sub(r'[\*~\^]',r'',text.lower()))

def is_known(word):
    return binary_search(word,knowns)

def word2int(word):
    if is_known(word):
        return word_indices[word]
    else:
        return vocab_size
    return vec

def word2vec(word):
    vec = [0] * (vocab_size + 1)
    vec[word2int(word)] = 1
    return vec

def tweet2vec(tweet):
    #assert(tweet[0] == '<tweet>' and tweet[-1] == '</tweet>')
    vec = [0] * (vocab_size + 1)
    for word in tweet:
        vec[word2int(word)] += 1
    return vec

def softmax(array):
    exps = [math.e**n for n in array]
    total = sum(exps)
    return [n/total for n in exps]

def magnitude(vec):
    return math.sqrt(np.dot(vec,vec))

def scale_vector(vec,length=1):
    mag = magnitude(vec)
    return [(x/mag)*length for x in vec]

def veccos(vec1,vec2):
    return np.dot(vec1,vec2)/(magnitude(vec1)*magnitude(vec2))

def angle(vec1,vec2):
    return np.arccos(veccos(vec1,vec2))

def classify(handle):
    statuses = get_timeline(handle)
    return classify(' '.join(statuses))

def classify_tweet(tweet):
    return classify(tweet)

def classify(string):
    tweet_vector = tweet2vec(preprocess(string))[:-1]
    similarities = [angle(tweet_vector,user_word_vectors[user]) for user in users]
    maximum = max(similarities)
    similarities = [maximum - value for value in similarities]
    return softmax(scale_vector(similarities, length=5))
