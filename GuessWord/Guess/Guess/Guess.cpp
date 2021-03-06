#pragma once

#include <iostream>
#include <string>
#include "FVocabularyGame.h"

using FText = std::string;
using int32 = int;

void Introduction(const FVocabularyGame& Game);
void PlayGame(FVocabularyGame& Game);
bool AskToPlayAgain();




int main()
{
	bool bPlayAgain = false;
	FVocabularyGame VocabularyGame;

	do
	{
		VocabularyGame.Reset();
		Introduction(VocabularyGame);
		PlayGame(VocabularyGame);
		bPlayAgain = AskToPlayAgain();
	} while (bPlayAgain);

	return 0;
}


void Introduction(const FVocabularyGame& Game)
{
	std::cout << "=========================\n";
	std::cout << "GAME: Guess a Word \n";
	std::cout << "Can you guess the " << Game.GetWordLength() << "-letter word ? \n";
	std::cout << std::endl;
}

void PlayGame(FVocabularyGame& Game)
{
	FText Word = "";
	while (Game.IsContinue())
	{
		Game.AskPlayer();
		Game.ChkAnswer();
	}
	Game.ShowAnswer();
}

bool AskToPlayAgain()
{
	FText Res = "";
	std::cout << "Play again ?(y/n)" << std::endl;
	std::getline(std::cin, Res);
	return (Res[0] == 'y' || Res[0] == 'Y');
}
