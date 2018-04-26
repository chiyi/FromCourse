#pragma once
#include <string>
using FText = std::string;
using int32 = int;


class FVocabularyGame
{
public:
	FVocabularyGame();
	~FVocabularyGame();

	void Reset();
	bool IsContinue() const;
	int32 GetWordLength() const;
	int32 GetMaxTries() const;
	void AskPlayer();
	void ChkAnswer();
	void ShowAnswer();

private:
	bool bIsWon;
	int32 NumTries;
	int32 MaxTries;
	FText HiddenWord;
	FText PlayerAns;
	int CountMatchedLetters(const FText &WordL, const FText &WordR);
	int CountMatchedAlphabets(const FText &WordL, const FText &WordR);
	void SetHiddenWord();
};

