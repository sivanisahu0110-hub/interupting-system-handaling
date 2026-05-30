Test Case 1:
Input: Silence
Expected: No interruption

Test Case 2:
Input: Fan noise
Expected: No interruption

Test Case 3:
Input: User speaks during TTS
Expected: TTS pauses

Test Case 4:
Input: User speaks after TTS ends
Expected: No interruption

Test Case 5:
Input: Multiple interruptions
Expected: Cooldown prevents repeated triggers