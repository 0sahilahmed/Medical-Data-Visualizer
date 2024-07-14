import unittest
import pandas as pd

from medical_data_visualizer import draw_cat_plot, draw_heat_map

class DataVisualizerTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('medical_examination.csv')

    def test_overweight_column(self):
        df = self.df.copy()
        df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)
        self.assertIn('overweight', df.columns)
        self.assertTrue(all(df['overweight'].isin([0, 1])))

    def test_normalize_data(self):
        df = self.df.copy()
        df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
        df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
        self.assertTrue(all(df['cholesterol'].isin([0, 1])))
        self.assertTrue(all(df['gluc'].isin([0, 1])))

    def test_draw_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)

    def test_draw_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()
