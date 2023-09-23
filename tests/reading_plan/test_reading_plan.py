from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import Mock, patch


@pytest.fixture
def mock_news():
    mocks = [
        {
            "url": "url_mock_1",
            "title": "mock_1",
            "timestamp": "01/01/2023",
            "writer": "Levy",
            "reading_time": 1,
            "summary": "Mock 1",
            "category": "News",
        },
        {
            "url": "url_mock_2",
            "title": "mock_2",
            "timestamp": "02/01/2023",
            "writer": "Levy",
            "reading_time": 2,
            "summary": "Mock 2",
            "category": "News",
        },
        {
            "url": "url_mock_3",
            "title": "mock_3",
            "timestamp": "03/01/2023",
            "writer": "Levy",
            "reading_time": 10,
            "summary": "Mock 3",
            "category": "News",
        },
    ]

    return mocks


@pytest.fixture
def mock_readable():
    mocks = [
        {
            'chosen_news': [('mock_1', 1), ('mock_2', 2)],
            'unfilled_time': 1,
        }
    ]

    return mocks


@pytest.fixture
def mock_unreadable():
    mocks = [
        ('mock_3', 10),
    ]

    return mocks


def test_reading_plan_group_news(mock_news, mock_readable, mock_unreadable):
    rp_service = ReadingPlanService()
    msg_ERRO = "Valor 'available_time' deve ser maior que zero"

    with pytest.raises(ValueError, match=msg_ERRO):
        rp_service.group_news_for_available_time(0)

    mock_find_news = Mock(return_value=mock_news)

    with patch("tech_news.analyzer.reading_plan.find_news", mock_find_news):
        result = rp_service.group_news_for_available_time(4)

    assert result["readable"] == mock_readable
    assert result["unreadable"] == mock_unreadable
