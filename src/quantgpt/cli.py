"""Command line interface for QuantGPT."""
import argparse
from .nlp import analyze_sentiment
from .forecasting import PriceForecaster
from .portfolio import optimize_portfolio


def main() -> None:
    parser = argparse.ArgumentParser(description="QuantGPT CLI")
    parser.add_argument("--sentiment", help="Text to analyze")
    parser.add_argument("--forecast", nargs="*", type=float, help="Prices for forecasting")
    args = parser.parse_args()

    if args.sentiment:
        score = analyze_sentiment(args.sentiment)
        print(f"Sentiment score: {score}")

    if args.forecast:
        model = PriceForecaster(args.forecast)
        print(model.forecast())


if __name__ == "__main__":
    main()
