class SimonGame
  COLORS = ["red", "green", "blue", "yellow"]

  def initialize
    @sequence = []
    @player_sequence = []
    @score = 0
  end

  def play
    puts "Welcome to Simon Game!"
    loop do
      add_random_color
      display_sequence
      get_player_sequence
      break unless correct_sequence?
      @score += 1
      puts "Correct! Your score is: #{@score}"
    end
    game_over
  end

  private

  def add_random_color
    @sequence << COLORS.sample
  end

  def display_sequence
    puts "Watch the sequence carefully!"
    @sequence.each do |color|
      puts color
      sleep(1)
      system("clear") || system("cls")
      sleep(0.5)
    end
  end

  def get_player_sequence
    @player_sequence.clear
    puts "Now it's your turn to repeat the sequence."
    @sequence.size.times do |i|
      print "Enter color ##{i + 1}: "
      @player_sequence << gets.chomp.downcase
    end
  end

  def correct_sequence?
    @sequence == @player_sequence
  end

  def game_over
    puts "Game Over! Your final score is: #{@score}"
  end
end

game = SimonGame.new
game.play
