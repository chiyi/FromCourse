#include "time.h"
#include "FVocabularyGame.h"
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>


FVocabularyGame::FVocabularyGame()
{
	this->Reset();
}


FVocabularyGame::~FVocabularyGame()
{
}

void FVocabularyGame::Reset()
{
	(*this).bIsWon = false;
	(*this).NumTries = 0;
	(*this).MaxTries = 10;
	(*this).SetHiddenWord();
	return;
}

void FVocabularyGame::SetHiddenWord()
{
	std::vector<FText> SomeWords = { "game", "rent", "compare", "red", "develop", "publicity", "round","deep","annoy","fortunate","seat","excellent","knotty","roof","sudden","meeting","aboriginal","multiply","keen","snake","imminent","small","stereotyped","rock","approval","lyrical","coordinated","outgoing","spiteful","incandescent","frog","team","psychedelic","irritating","fertile","irritate","low","observation","bouncy","water","complete","fear","beneficial","page","shocking","face","fact","ruin","four","puzzled","zoom","laughable","tacky","remarkable","satisfying","vigorous","tight","voracious","afterthought","melted","land","wrathful","face","look","trouble","vagabond","hand","compete","obey","cemetery","deliver","alleged","list","join","depend","credit","order","zinc","overrated","squeeze","silk","preach","floor","lumpy","eye","changeable","scale","fasten","produce","sophisticated","protest","found","massive","match","discreet","tire","cooing","crash","bore","frail","lock","striped","tremendous","ugliest","intelligent","resolute","plantation" };
	int NWords = SomeWords.size();
	srand((unsigned)time(0));
	int IndexPick = rand() % NWords;
	(*this).HiddenWord = SomeWords[IndexPick];
}

int32 FVocabularyGame::GetWordLength() const
{
	return (*this).HiddenWord.length();
}

int32 FVocabularyGame::GetMaxTries() const
{
	return (*this).MaxTries;
}

bool FVocabularyGame::IsContinue() const
{
	bool Res = ((*this).bIsWon || (*this).NumTries > (*this).MaxTries) ? false : true;
	return Res;
}

void FVocabularyGame::AskPlayer()
{
	FText Res = "";

	bool bChk = false;
	do
	{
		std::cout << "Try #" << (*this).NumTries << " of " << (*this).GetMaxTries() << ".\n";
		std::cout << "Enter your guess: ";
		std::getline(std::cin, Res);

		bChk = (Res.length() == (*this).GetWordLength()) ? true : false;
	} while (bChk == false);

	(*this).NumTries++;
	transform(Res.begin(), Res.end(), Res.begin(), ::tolower);
	(*this).PlayerAns = Res;
}

void FVocabularyGame::ChkAnswer()
{
	int NTrueLetter = 0;
	int NUniqAlphabets = 0;
	FText WordL = (*this).PlayerAns;
	FText WordR = (*this).HiddenWord;

	if (WordL == WordR)
	{
		bIsWon = true;
		std::cout << "Correct !\n";
	}
	else
	{
		NTrueLetter = CountMatchedLetters(WordL, WordR);
		NUniqAlphabets = CountMatchedAlphabets(WordL, WordR);
		std::cout << "N_MatchedLetters = " << NTrueLetter << ", ";
		std::cout << "N_MatchedUniqAlphabets = " << NUniqAlphabets << "\n";
	}
}

int FVocabularyGame::CountMatchedLetters(const FText &WordL, const FText &WordR)
{
	int Res = -1;
	if (WordL.length() == WordR.length())
	{
		Res = 0;
		for (unsigned int idx = 0; idx < WordL.length(); idx++)
		{
			Res += (WordL[idx] == WordR[idx] ? 1 : 0);
		}
	}
	return Res;
}

int FVocabularyGame::CountMatchedAlphabets(const FText &WordL, const FText &WordR)
{
	int Res = -1;
	std::set<char> Alpha_L, Alpha_R;

	if (WordL.length() == WordR.length())
	{
		Res = 0;

		for (unsigned int idx = 0; idx < WordL.length(); idx++)
		{
			Alpha_L.insert(WordL[idx]);
			Alpha_R.insert(WordR[idx]);
		}

		for (std::set<char>::iterator it = Alpha_L.begin(); it!=Alpha_L.end(); it++)
		{
			Res += (Alpha_R.find(*it) != Alpha_R.end() ? 1 : 0);
		}
	}
	return Res;
}

void FVocabularyGame::ShowAnswer()
{
	std::cout << "Answer = " << (*this).HiddenWord << "\n";
}