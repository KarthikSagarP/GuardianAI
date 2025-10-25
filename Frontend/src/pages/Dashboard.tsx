import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import {
  Shield,
  MessageSquare,
  Sparkles,
  Github,
  FileText,
  Zap,
} from 'lucide-react';

const Dashboard = () => {
  const features = [
    {
      icon: Shield,
      title: 'Code Audit',
      description: 'Scan repositories for compliance violations',
      gradient: 'from-red-500 to-orange-500',
      link: '/audit',
    },
    {
      icon: MessageSquare,
      title: 'Q&A Assistant',
      description: 'Ask questions about your codebase',
      gradient: 'from-blue-500 to-cyan-500',
      link: '/qa',
    },
    {
      icon: Sparkles,
      title: 'AI Agent',
      description: 'Natural language compliance analysis',
      gradient: 'from-purple-500 to-pink-500',
      link: '/agent',
    },
  ];

  const stats = [
    { label: 'Repositories Scanned', value: '1,234+', icon: Github },
    { label: 'Violations Detected', value: '5,678+', icon: Shield },
    { label: 'Questions Answered', value: '10K+', icon: MessageSquare },
  ];

  return (
    <div className="min-h-screen p-8">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center mb-16"
      >
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary-100 dark:bg-primary-900/30 mb-6">
          <Zap className="w-4 h-4 text-primary-600 dark:text-primary-400" />
          <span className="text-sm font-semibold text-primary-600 dark:text-primary-400">
            Powered by AI
          </span>
        </div>

        <h1 className="text-6xl font-bold mb-6">
          <span className="gradient-text">Guardian AI</span>
        </h1>
        <p className="text-xl text-gray-600 dark:text-slate-400 max-w-2xl mx-auto">
          Your intelligent compliance and code analysis platform. Detect
          violations, understand codebases, and ensure regulatory compliance.
        </p>
      </motion.div>

      {/* Feature Cards */}
      <div className="grid md:grid-cols-3 gap-8 mb-16 max-w-6xl mx-auto">
        {features.map((feature, index) => (
          <motion.div
            key={feature.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
          >
            <Link to={feature.link}>
              <div className="card group hover:scale-105 cursor-pointer">
                <div
                  className={`w-16 h-16 rounded-2xl bg-gradient-to-br ${feature.gradient} 
                  flex items-center justify-center mb-4 group-hover:shadow-lg transition-all`}
                >
                  <feature.icon className="w-8 h-8 text-white" />
                </div>
                <h3 className="text-2xl font-bold mb-2 text-gray-900 dark:text-slate-50">
                  {feature.title}
                </h3>
                <p className="text-gray-600 dark:text-slate-400">
                  {feature.description}
                </p>
              </div>
            </Link>
          </motion.div>
        ))}
      </div>

      {/* Stats Section */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className="glass-panel p-8 max-w-4xl mx-auto"
      >
        <div className="grid md:grid-cols-3 gap-8">
          {stats.map((stat, index) => (
            <div key={stat.label} className="text-center">
              <div className="flex justify-center mb-3">
                <stat.icon className="w-8 h-8 text-primary-500 dark:text-primary-400" />
              </div>
              <div className="text-3xl font-bold text-gray-900 dark:text-slate-50 mb-1">
                {stat.value}
              </div>
              <div className="text-sm text-gray-600 dark:text-slate-400">
                {stat.label}
              </div>
            </div>
          ))}
        </div>
      </motion.div>

      {/* Quick Start Guide */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4 }}
        className="max-w-4xl mx-auto mt-16"
      >
        <h2 className="text-3xl font-bold text-center mb-8 text-gray-900 dark:text-slate-50">
          How It Works
        </h2>
        <div className="grid md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="w-12 h-12 rounded-full bg-primary-500 text-white font-bold text-xl flex items-center justify-center mx-auto mb-4">
              1
            </div>
            <h3 className="font-semibold mb-2 text-gray-900 dark:text-slate-50">
              Choose Analysis Type
            </h3>
            <p className="text-sm text-gray-600 dark:text-slate-400">
              Select code audit, Q&A, or AI agent mode
            </p>
          </div>
          <div className="text-center">
            <div className="w-12 h-12 rounded-full bg-primary-500 text-white font-bold text-xl flex items-center justify-center mx-auto mb-4">
              2
            </div>
            <h3 className="font-semibold mb-2 text-gray-900 dark:text-slate-50">
              Input Repository
            </h3>
            <p className="text-sm text-gray-600 dark:text-slate-400">
              Provide GitHub URL and compliance documents
            </p>
          </div>
          <div className="text-center">
            <div className="w-12 h-12 rounded-full bg-primary-500 text-white font-bold text-xl flex items-center justify-center mx-auto mb-4">
              3
            </div>
            <h3 className="font-semibold mb-2 text-gray-900 dark:text-slate-50">
              Get Insights
            </h3>
            <p className="text-sm text-gray-600 dark:text-slate-400">
              Receive detailed analysis and recommendations
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Dashboard;
